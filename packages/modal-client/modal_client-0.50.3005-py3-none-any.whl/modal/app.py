# Copyright Modal Labs 2022
from typing import TYPE_CHECKING, Any, Dict, Optional, Sequence, TypeVar

from google.protobuf.message import Message

from modal_proto import api_pb2
from modal_utils.async_utils import synchronize_api
from modal_utils.grpc_utils import get_proto_oneof, retry_transient_errors

from ._output import OutputManager
from ._resolver import Resolver
from .client import _Client
from .config import logger
from .gpu import GPU_T
from .object import _Provider

if TYPE_CHECKING:
    from rich.tree import Tree

    import modal.image
    import modal.sandbox
else:
    Tree = TypeVar("Tree")


class _App:
    """Apps are the user representation of an actively running Modal process.

    You can obtain an `App` from the `Stub.run()` context manager. While the app
    is running, you can get its `app_id`, `client`, and other useful properties
    from this object.

    ```python
    import modal

    stub = modal.Stub()
    stub.my_secret_object = modal.Secret.from_name("my-secret")

    if __name__ == "__main__":
        with stub.run() as app:
            print(app.client)
            print(app.app_id)
            print(app.my_secret_object)
    ```
    """

    _tag_to_object: Dict[str, _Provider]
    _tag_to_object_id: Dict[str, str]
    _tag_to_handle_metadata: Dict[str, Message]

    _client: _Client
    _app_id: str
    _app_page_url: str
    _resolver: Optional[Resolver]
    _environment_name: str
    _output_mgr: Optional[OutputManager]
    _associated_stub: Optional[Any]  # TODO(erikbern): type

    def __init__(
        self,
        client: _Client,
        app_id: str,
        app_page_url: str,
        output_mgr: Optional[OutputManager],
        tag_to_object: Optional[Dict[str, _Provider]] = None,
        tag_to_object_id: Optional[Dict[str, str]] = None,
        stub_name: Optional[str] = None,
        environment_name: Optional[str] = None,
    ):
        """mdmd:hidden This is the app constructor. Users should not call this directly."""
        self._app_id = app_id
        self._app_page_url = app_page_url
        self._client = client
        self._tag_to_object = tag_to_object or {}
        self._tag_to_object_id = tag_to_object_id or {}
        self._tag_to_handle_metadata = {}
        self._stub_name = stub_name
        self._environment_name = environment_name
        self._output_mgr = output_mgr
        self._associated_stub = None

    @property
    def client(self) -> _Client:
        """A reference to the running App's server client."""
        return self._client

    @property
    def app_id(self) -> str:
        """A unique identifier for this running App."""
        return self._app_id

    def _associate_stub(self, stub):
        if self._associated_stub:
            if self._stub_name:
                warning_sub_message = f"stub with the same name ('{self._stub_name}')"
            else:
                warning_sub_message = "unnamed stub"
            logger.warning(
                f"You have more than one {warning_sub_message}. It's recommended to name all your Stubs uniquely when using multiple stubs"
            )
        self._associated_stub = stub

        # Initialize objects on stub
        stub_objects: dict[str, _Provider] = {}
        if stub:
            stub_objects = dict(stub.get_objects())
        for tag, object_id in self._tag_to_object_id.items():
            handle_metadata = self._tag_to_handle_metadata.get(tag)
            if tag in stub_objects:
                # This already exists on the stub (typically a function)
                provider = stub_objects[tag]
                provider._handle._hydrate(object_id, self._client, handle_metadata)
            else:
                # Can't find the object, create a new one
                provider = _Provider._new_hydrated(object_id, self._client, handle_metadata)
            self._tag_to_object[tag] = provider

    async def _create_all_objects(
        self, blueprint: Dict[str, _Provider], new_app_state: int, environment_name: str, shell: bool = False
    ):  # api_pb2.AppState.V
        """Create objects that have been defined but not created on the server."""
        resolver = Resolver(
            self._client,
            output_mgr=self._output_mgr,
            environment_name=environment_name,
            app_id=self.app_id,
            shell=shell,
        )
        with resolver.display():
            # Get current objects, and reset all objects
            tag_to_object_id = self._tag_to_object_id
            self._tag_to_object_id = {}

            # Assign all objects
            for tag, provider in blueprint.items():
                self._tag_to_object[tag] = provider

                # Reset object_id in case the app runs twice
                # TODO(erikbern): clean up the interface
                provider._handle._init()

            # Preload all functions to make sure they have ids assigned before they are loaded.
            # This is important to make sure any enclosed function handle references in serialized
            # functions have ids assigned to them when the function is serialized.
            # Note: when handles/providers are merged, all objects will need to get ids pre-assigned
            # like this in order to be referrable within serialized functions
            for tag, provider in blueprint.items():
                existing_object_id = tag_to_object_id.get(tag)
                # Note: preload only currently implemented for Functions, returns None otherwise
                # this is to ensure that directly referenced functions from the global scope has
                # ids associated with them when they are serialized into other functions
                await resolver.preload(provider, existing_object_id)
                if provider.object_id is not None:
                    tag_to_object_id[tag] = provider.object_id

            for tag, provider in blueprint.items():
                existing_object_id = tag_to_object_id.get(tag)
                await resolver.load(provider, existing_object_id)
                self._tag_to_object_id[tag] = provider.object_id

        # Create the app (and send a list of all tagged obs)
        # TODO(erikbern): we should delete objects from a previous version that are no longer needed
        # We just delete them from the app, but the actual objects will stay around
        indexed_object_ids = self._tag_to_object_id
        assert indexed_object_ids == self._tag_to_object_id
        all_objects = resolver.objects()

        unindexed_object_ids = list(
            set(obj.object_id for obj in all_objects) - set(obj.object_id for obj in self._tag_to_object.values())
        )
        req_set = api_pb2.AppSetObjectsRequest(
            app_id=self._app_id,
            indexed_object_ids=indexed_object_ids,
            unindexed_object_ids=unindexed_object_ids,
            new_app_state=new_app_state,  # type: ignore
        )
        await retry_transient_errors(self._client.stub.AppSetObjects, req_set)
        return self._tag_to_object

    async def disconnect(self):
        """Tell the server the client has disconnected for this app. Terminates all running tasks
        for ephemeral apps."""

        logger.debug("Sending app disconnect/stop request")
        req_disconnect = api_pb2.AppClientDisconnectRequest(app_id=self._app_id)
        await retry_transient_errors(self._client.stub.AppClientDisconnect, req_disconnect)
        logger.debug("App disconnected")

    async def stop(self):
        """Tell the server to stop this app, terminating all running tasks."""
        req_disconnect = api_pb2.AppStopRequest(app_id=self._app_id)
        await retry_transient_errors(self._client.stub.AppStop, req_disconnect)

    def log_url(self):
        return self._app_page_url

    def __getitem__(self, tag: str) -> _Provider:
        # Deprecated?
        return self._tag_to_object[tag]

    def __contains__(self, tag: str) -> bool:
        return tag in self._tag_to_object

    def __getattr__(self, tag: str) -> _Provider:
        return self._tag_to_object[tag]

    async def _init_container(self, client: _Client, app_id: str, stub_name: str):
        self._client = client
        self._app_id = app_id
        self._stub_name = stub_name
        req = api_pb2.AppGetObjectsRequest(app_id=self._app_id)
        resp = await retry_transient_errors(self._client.stub.AppGetObjects, req)
        for item in resp.items:
            self._tag_to_object_id[item.tag] = item.object_id
            handle_metadata: Optional[Message] = get_proto_oneof(item, "handle_metadata_oneof")
            if handle_metadata is not None:
                self._tag_to_handle_metadata[item.tag] = handle_metadata

    @staticmethod
    async def init_container(client: _Client, app_id: str, stub_name: str = "") -> "_App":
        """Used by the container to bootstrap the app and all its objects. Not intended to be called by Modal users."""
        global _container_app, _is_container_app
        _is_container_app = True
        await _container_app._init_container(client, app_id, stub_name)
        return _container_app

    @staticmethod
    async def _init_existing(
        client: _Client, existing_app_id: str, output_mgr: Optional[OutputManager] = None
    ) -> "_App":
        # Get all the objects first
        obj_req = api_pb2.AppGetObjectsRequest(app_id=existing_app_id)
        obj_resp = await retry_transient_errors(client.stub.AppGetObjects, obj_req)
        app_page_url = f"https://modal.com/apps/{existing_app_id}"  # TODO (elias): this should come from the backend
        object_ids = {item.tag: item.object_id for item in obj_resp.items}
        return _App(client, existing_app_id, app_page_url, output_mgr, tag_to_object_id=object_ids)

    @staticmethod
    async def _init_new(
        client: _Client,
        description: Optional[str] = None,
        detach: bool = False,
        deploying: bool = False,
        environment_name: str = "",
        output_mgr: Optional[OutputManager] = None,
    ) -> "_App":
        # Start app
        # TODO(erikbern): maybe this should happen outside of this method?
        app_req = api_pb2.AppCreateRequest(
            description=description,
            initializing=deploying,
            detach=detach,
            environment_name=environment_name,
        )
        app_resp = await retry_transient_errors(client.stub.AppCreate, app_req)
        app_page_url = app_resp.app_logs_url
        logger.debug(f"Created new app with id {app_resp.app_id}")
        return _App(client, app_resp.app_id, app_page_url, output_mgr, environment_name=environment_name)

    @staticmethod
    async def _init_from_name(
        client: _Client,
        name: str,
        namespace,
        environment_name: str = "",
        output_mgr: Optional[OutputManager] = None,
    ):
        # Look up any existing deployment
        app_req = api_pb2.AppGetByDeploymentNameRequest(
            name=name, namespace=namespace, environment_name=environment_name
        )
        app_resp = await retry_transient_errors(client.stub.AppGetByDeploymentName, app_req)
        existing_app_id = app_resp.app_id or None

        # Grab the app
        if existing_app_id is not None:
            return await _App._init_existing(client, existing_app_id, output_mgr=output_mgr)
        else:
            return await _App._init_new(
                client, name, detach=False, deploying=True, environment_name=environment_name, output_mgr=output_mgr
            )

    async def create_one_object(self, provider: _Provider, environment_name: str) -> None:
        existing_object_id: Optional[str] = self._tag_to_object_id.get("_object")
        resolver = Resolver(self._client, environment_name=environment_name, app_id=self.app_id)
        await resolver.load(provider, existing_object_id)
        indexed_object_ids = {"_object": provider.object_id}
        unindexed_object_ids = [obj.object_id for obj in resolver.objects() if obj.object_id is not provider.object_id]
        req_set = api_pb2.AppSetObjectsRequest(
            app_id=self.app_id,
            indexed_object_ids=indexed_object_ids,
            unindexed_object_ids=unindexed_object_ids,
            new_app_state=api_pb2.APP_STATE_UNSPECIFIED,  # app is either already deployed or will be set to deployed after this call
        )
        await retry_transient_errors(self._client.stub.AppSetObjects, req_set)

    async def deploy(self, name: str, namespace, object_entity: str) -> str:
        deploy_req = api_pb2.AppDeployRequest(
            app_id=self.app_id,
            name=name,
            namespace=namespace,
            object_entity=object_entity,
        )
        deploy_response = await retry_transient_errors(self._client.stub.AppDeploy, deploy_req)
        return deploy_response.url

    async def spawn_sandbox(
        self,
        *entrypoint_args: str,
        image: Optional["modal.image._Image"] = None,  # The image to run as the container for the sandbox.
        mounts: Sequence["modal.image._Mount"] = (),
        timeout: Optional[int] = None,  # Maximum execution time of the sandbox in seconds.
        workdir: Optional[str] = None,  # Working directory of the sandbox.
        gpu: GPU_T = None,
        cloud: Optional[str] = None,
        cpu: Optional[float] = None,  # How many CPU cores to request. This is a soft limit.
        memory: Optional[int] = None,  # How much memory to request, in MiB. This is a soft limit.
    ) -> "modal.sandbox._Sandbox":
        """Sandboxes are a way to run arbitrary commands in dynamically defined environments.

        This function returns a [SandboxHandle](/docs/reference/modal.Sandbox#modalsandboxsandboxhandle), which can be used to interact with the running sandbox.

        Refer to the [docs](/docs/guide/sandbox) on how to spawn and use sandboxes.
        """
        from .sandbox import _Sandbox
        from .stub import _default_image

        self._client.track_function_invocation()

        resolver = Resolver(self._client, environment_name=self._environment_name, app_id=self.app_id)
        provider = _Sandbox._new(
            entrypoint_args,
            image=image or _default_image,
            mounts=mounts,
            timeout=timeout,
            workdir=workdir,
            gpu=gpu,
            cloud=cloud,
            cpu=cpu,
            memory=memory,
        )
        await resolver.load(provider)
        return provider

    @staticmethod
    def _reset_container():
        # Just used for tests
        global _is_container_app, _container_app
        _is_container_app = False
        _container_app.__init__(None, None, None, None)  # type: ignore


App = synchronize_api(_App)

_is_container_app = False
_container_app = _App(None, None, None, None)
container_app = synchronize_api(_container_app)
assert isinstance(container_app, App)
__doc__container_app = """A reference to the running `modal.App`, accessible from within a running Modal function.
Useful for accessing object handles for any Modal objects declared on the stub, e.g:

```python
stub = modal.Stub()
stub.data = modal.Dict()

@stub.function()
def store_something(key, value):
    data: modal.Dict = modal.container_app.data
    data.put(key, value)
```
"""


def is_local() -> bool:
    """Returns if we are currently on the machine launching/deploying a Modal app

    Returns `True` when executed locally on the user's machine.
    Returns `False` when executed from a Modal container in the cloud.
    """
    return not _is_container_app

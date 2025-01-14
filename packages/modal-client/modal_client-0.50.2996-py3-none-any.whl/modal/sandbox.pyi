import modal.client
import modal.image
import modal.mount
import modal.object
import modal_proto.api_pb2
import typing
import typing_extensions

class _LogsReader:
    def __init__(self, file_descriptor: int, sandbox_id: str, client: modal.client._Client) -> None:
        ...

    async def read(self) -> str:
        ...


class LogsReader:
    def __init__(self, file_descriptor: int, sandbox_id: str, client: modal.client.Client) -> None:
        ...

    class __read_spec(typing_extensions.Protocol):
        def __call__(self) -> str:
            ...

        async def aio(self, *args, **kwargs) -> str:
            ...

    read: __read_spec


class _SandboxHandle(modal.object._Handle):
    _result: typing.Union[modal_proto.api_pb2.GenericResult, None]
    _stdout: _LogsReader
    _stderr: _LogsReader

    async def wait(self):
        ...

    @property
    def stdout(self) -> _LogsReader:
        ...

    @property
    def stderr(self) -> _LogsReader:
        ...

    @property
    def returncode(self) -> typing.Union[int, None]:
        ...


class SandboxHandle(modal.object.Handle):
    _result: typing.Union[modal_proto.api_pb2.GenericResult, None]
    _stdout: LogsReader
    _stderr: LogsReader

    def __init__(self):
        ...

    class __wait_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    wait: __wait_spec

    @property
    def stdout(self) -> LogsReader:
        ...

    @property
    def stderr(self) -> LogsReader:
        ...

    @property
    def returncode(self) -> typing.Union[int, None]:
        ...


class _Sandbox(modal.object._Provider):
    @staticmethod
    def _new(entrypoint_args: typing.Sequence[str], image: modal.image._Image, mounts: typing.Sequence[modal.mount._Mount], timeout: typing.Union[int, None] = None, workdir: typing.Union[str, None] = None) -> _SandboxHandle:
        ...

    async def wait(self):
        ...

    @property
    def stdout(self) -> _LogsReader:
        ...

    @property
    def stderr(self) -> _LogsReader:
        ...

    @property
    def returncode(self) -> typing.Union[int, None]:
        ...


class Sandbox(modal.object.Provider):
    def __init__(self):
        ...

    @staticmethod
    def _new(entrypoint_args: typing.Sequence[str], image: modal.image.Image, mounts: typing.Sequence[modal.mount.Mount], timeout: typing.Union[int, None] = None, workdir: typing.Union[str, None] = None) -> SandboxHandle:
        ...

    class __wait_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    wait: __wait_spec

    @property
    def stdout(self) -> LogsReader:
        ...

    @property
    def stderr(self) -> LogsReader:
        ...

    @property
    def returncode(self) -> typing.Union[int, None]:
        ...

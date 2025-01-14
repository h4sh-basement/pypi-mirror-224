# Copyright Modal Labs 2022
import io
import pickle

import cloudpickle

from .exception import InvalidError
from .object import Handle, Provider, _Handle, _Provider

PICKLE_PROTOCOL = 4  # Support older Python versions.


class Pickler(cloudpickle.Pickler):
    def __init__(self, buf):
        super().__init__(buf, protocol=PICKLE_PROTOCOL)

    def persistent_id(self, obj):
        if isinstance(obj, _Handle):
            flag = "_h"
        elif isinstance(obj, Handle):
            flag = "h"
        elif isinstance(obj, _Provider):
            flag = "_p"
        elif isinstance(obj, Provider):
            flag = "p"
        else:
            return
        if not obj.object_id:
            raise InvalidError(f"Can't serialize object {obj} which hasn't been created.")
        return (obj.object_id, flag, obj._get_metadata())


class Unpickler(pickle.Unpickler):
    def __init__(self, client, buf):
        self.client = client
        super().__init__(buf)

    def persistent_load(self, pid):
        (object_id, flag, handle_proto) = pid
        if flag == "h":
            return Handle._new_hydrated(object_id, self.client, handle_proto)
        elif flag == "_h":
            return _Handle._new_hydrated(object_id, self.client, handle_proto)
        elif flag == "p":
            return Provider._new_hydrated(object_id, self.client, handle_proto)
        elif flag == "_p":
            return _Provider._new_hydrated(object_id, self.client, handle_proto)
        else:
            raise InvalidError("bad flag")


def serialize(obj):
    """Serializes object and replaces all references to the client class by a placeholder."""
    buf = io.BytesIO()
    Pickler(buf).dump(obj)
    return buf.getvalue()


def deserialize(s: bytes, client):
    """Deserializes object and replaces all client placeholders by self."""
    return Unpickler(client, io.BytesIO(s)).load()

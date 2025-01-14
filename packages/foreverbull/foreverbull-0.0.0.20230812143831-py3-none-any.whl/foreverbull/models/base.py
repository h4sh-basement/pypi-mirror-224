import json
from typing import Union

from pydantic import BaseModel


class Base(BaseModel):
    @classmethod
    def load(cls, data: Union[dict, bytes]) -> object:
        if type(data) is dict:
            return cls(**data)
        loaded = json.loads(data.decode())
        return cls(**loaded)

    def dump(self) -> bytes:
        return self.model_dump_json().encode()

    def update_fields(self, object: dict):
        for key, value in object.items():
            if key in self.__fields__:
                setattr(self, key, value)
        return self

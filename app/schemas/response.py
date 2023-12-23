from pydantic.generics import GenericModel
from pydantic.main import BaseModel
from pydantic import validator
from typing import Generic, TypeVar, Optional

DataT = TypeVar('DataT')


class Response(GenericModel, Generic[DataT]):
    data: Optional[DataT]
    msg: Optional[str]
    code: int = 0

    # @classmethod
    @validator('msg', always=True)
    def check_msg(cls, v, values):
        if v is not None and values.get("data") is not None:
            raise ValueError("must not provide both data and msg")
        if v is None and values.get("data") is None:
            raise ValueError("must provide data or msg")

        return v

    # @classmethod
    @validator("code", always=True)
    def check_code(cls, v, values):
        if v == 0 and values.get("data") is None:
            raise ValueError("code must be 0 if data is provided")
        if v > 0 and (values.get("msg") is None or values.get("msg").strip() == ""):
            raise ValueError("code must not be 0 if msg is provided")

        return v

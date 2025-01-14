# coding: utf-8

"""
    Edge Impulse API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, validator

class MoveRawDataRequest(BaseModel):
    new_category: StrictStr = Field(..., alias="newCategory")
    __properties = ["newCategory"]

    @validator('new_category')
    def new_category_validate_enum(cls, v):
        if v not in ('training', 'testing', 'anomaly'):
            raise ValueError("must validate the enum values ('training', 'testing', 'anomaly')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = False

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MoveRawDataRequest:
        """Create an instance of MoveRawDataRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MoveRawDataRequest:
        """Create an instance of MoveRawDataRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MoveRawDataRequest.construct(**obj)

        _obj = MoveRawDataRequest.construct(**{
            "new_category": obj.get("newCategory")
        })
        return _obj


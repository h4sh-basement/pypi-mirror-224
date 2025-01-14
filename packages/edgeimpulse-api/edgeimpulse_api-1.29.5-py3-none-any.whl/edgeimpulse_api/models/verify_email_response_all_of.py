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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class VerifyEmailResponseAllOf(BaseModel):
    email: Optional[StrictStr] = Field(None, description="Email address that was verified.")
    user_id: Optional[float] = Field(None, alias="userId", description="ID of the user associated with the verified email address, if any.")
    redirect_url: Optional[StrictStr] = Field(None, alias="redirectUrl", description="URL to redirect the user to after email verification.")
    __properties = ["email", "userId", "redirectUrl"]

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
    def from_json(cls, json_str: str) -> VerifyEmailResponseAllOf:
        """Create an instance of VerifyEmailResponseAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyEmailResponseAllOf:
        """Create an instance of VerifyEmailResponseAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return VerifyEmailResponseAllOf.construct(**obj)

        _obj = VerifyEmailResponseAllOf.construct(**{
            "email": obj.get("email"),
            "user_id": obj.get("userId"),
            "redirect_url": obj.get("redirectUrl")
        })
        return _obj


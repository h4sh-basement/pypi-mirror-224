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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class CreateEnterpriseTrialUserRequestAllOf(BaseModel):
    name: StrictStr = Field(..., description="Name of the user.")
    username: StrictStr = Field(..., description="Username, minimum 4 and maximum 30 characters. May contain alphanumeric characters, hyphens, underscores and dots. Validated according to `^(?=.{4,30}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._-]+(?<![_.])$`.")
    email: StrictStr = Field(..., description="Email of the user. Only business email addresses are allowed. Emails with free domains like gmail.com or yahoo.com are not allowed.")
    privacy_policy: StrictBool = Field(..., alias="privacyPolicy", description="Whether the user has accepted the terms of service and privacy policy.")
    password: Optional[StrictStr] = Field(None, description="Password of the user. Minimum length 8 characters.")
    job_title: Optional[StrictStr] = Field(None, alias="jobTitle", description="Job title of the user.")
    company_name: Optional[StrictStr] = Field(None, alias="companyName", description="Name of the company requesting the trial.")
    __properties = ["name", "username", "email", "privacyPolicy", "password", "jobTitle", "companyName"]

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
    def from_json(cls, json_str: str) -> CreateEnterpriseTrialUserRequestAllOf:
        """Create an instance of CreateEnterpriseTrialUserRequestAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateEnterpriseTrialUserRequestAllOf:
        """Create an instance of CreateEnterpriseTrialUserRequestAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateEnterpriseTrialUserRequestAllOf.construct(**obj)

        _obj = CreateEnterpriseTrialUserRequestAllOf.construct(**{
            "name": obj.get("name"),
            "username": obj.get("username"),
            "email": obj.get("email"),
            "privacy_policy": obj.get("privacyPolicy"),
            "password": obj.get("password"),
            "job_title": obj.get("jobTitle"),
            "company_name": obj.get("companyName")
        })
        return _obj


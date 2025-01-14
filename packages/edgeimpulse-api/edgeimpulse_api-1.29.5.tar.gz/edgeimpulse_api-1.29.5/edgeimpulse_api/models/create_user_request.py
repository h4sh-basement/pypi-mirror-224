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

class CreateUserRequest(BaseModel):
    name: StrictStr = Field(..., description="Your name")
    username: StrictStr = Field(..., description="Username, minimum 4 and maximum 30 characters. May contain alphanumeric characters, hyphens, underscores and dots. Validated according to `^(?=.{4,30}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._-]+(?<![_.])$`.")
    email: StrictStr = Field(..., description="E-mail address. Will need to be validated before the account will become active.")
    password: Optional[StrictStr] = Field(None, description="Password, minimum length 8 characters.")
    project_name: Optional[StrictStr] = Field(None, alias="projectName", description="A project will automatically be created. Sets the name of the first project. If not set, this will be derived from the username.")
    privacy_policy: StrictBool = Field(..., alias="privacyPolicy", description="Whether the user accepted the privacy policy")
    activation_token: Optional[StrictStr] = Field(None, alias="activationToken", description="Activation token for users created via SSO")
    identity_provider: Optional[StrictStr] = Field(None, alias="identityProvider", description="Unique identifier of the identity provider asserting the identity of this user")
    job_title: Optional[StrictStr] = Field(None, alias="jobTitle", description="Job title of the user. Optional field")
    session_id: Optional[StrictStr] = Field(None, alias="sessionId", description="Session ID. Optional field")
    company_name: Optional[StrictStr] = Field(None, alias="companyName", description="ACME Inc.")
    __properties = ["name", "username", "email", "password", "projectName", "privacyPolicy", "activationToken", "identityProvider", "jobTitle", "sessionId", "companyName"]

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
    def from_json(cls, json_str: str) -> CreateUserRequest:
        """Create an instance of CreateUserRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateUserRequest:
        """Create an instance of CreateUserRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateUserRequest.construct(**obj)

        _obj = CreateUserRequest.construct(**{
            "name": obj.get("name"),
            "username": obj.get("username"),
            "email": obj.get("email"),
            "password": obj.get("password"),
            "project_name": obj.get("projectName"),
            "privacy_policy": obj.get("privacyPolicy"),
            "activation_token": obj.get("activationToken"),
            "identity_provider": obj.get("identityProvider"),
            "job_title": obj.get("jobTitle"),
            "session_id": obj.get("sessionId"),
            "company_name": obj.get("companyName")
        })
        return _obj


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
from pydantic import BaseModel, Field, StrictStr, validator

class SendUserFeedbackRequest(BaseModel):
    type: StrictStr = ...
    subject: StrictStr = Field(..., description="The reason the user is contacting Edge Impulse Support.")
    body: StrictStr = Field(..., description="The body of the message.")
    work_email: Optional[StrictStr] = Field(None, alias="workEmail", description="The user's work email address. This is optional, if it's not provided, the registered email will be used.")
    company: Optional[StrictStr] = Field(None, description="The user's company. This is optional.")
    job_title: Optional[StrictStr] = Field(None, alias="jobTitle", description="The user's job title. This is optional.")
    company_size: Optional[StrictStr] = Field(None, alias="companySize", description="The user's company size. This is optional.")
    organization_id: Optional[float] = Field(None, alias="organizationId", description="The user's organization ID. This is optional.")
    __properties = ["type", "subject", "body", "workEmail", "company", "jobTitle", "companySize", "organizationId"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v not in ('feedback', 'sales'):
            raise ValueError("must validate the enum values ('feedback', 'sales')")
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
    def from_json(cls, json_str: str) -> SendUserFeedbackRequest:
        """Create an instance of SendUserFeedbackRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SendUserFeedbackRequest:
        """Create an instance of SendUserFeedbackRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SendUserFeedbackRequest.construct(**obj)

        _obj = SendUserFeedbackRequest.construct(**{
            "type": obj.get("type"),
            "subject": obj.get("subject"),
            "body": obj.get("body"),
            "work_email": obj.get("workEmail"),
            "company": obj.get("company"),
            "job_title": obj.get("jobTitle"),
            "company_size": obj.get("companySize"),
            "organization_id": obj.get("organizationId")
        })
        return _obj


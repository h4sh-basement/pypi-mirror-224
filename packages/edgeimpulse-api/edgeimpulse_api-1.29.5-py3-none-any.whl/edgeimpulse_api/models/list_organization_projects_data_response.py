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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects import ListOrganizationProjectsDataResponseAllOfProjects
from edgeimpulse_api.models.sample import Sample

class ListOrganizationProjectsDataResponse(BaseModel):
    success: StrictBool = Field(..., description="Whether the operation succeeded")
    error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
    projects: List[ListOrganizationProjectsDataResponseAllOfProjects] = ...
    samples: List[Sample] = ...
    __properties = ["success", "error", "projects", "samples"]

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
    def from_json(cls, json_str: str) -> ListOrganizationProjectsDataResponse:
        """Create an instance of ListOrganizationProjectsDataResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in projects (list)
        _items = []
        if self.projects:
            for _item in self.projects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['projects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in samples (list)
        _items = []
        if self.samples:
            for _item in self.samples:
                if _item:
                    _items.append(_item.to_dict())
            _dict['samples'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListOrganizationProjectsDataResponse:
        """Create an instance of ListOrganizationProjectsDataResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ListOrganizationProjectsDataResponse.construct(**obj)

        _obj = ListOrganizationProjectsDataResponse.construct(**{
            "success": obj.get("success"),
            "error": obj.get("error"),
            "projects": [ListOrganizationProjectsDataResponseAllOfProjects.from_dict(_item) for _item in obj.get("projects")] if obj.get("projects") is not None else None,
            "samples": [Sample.from_dict(_item) for _item in obj.get("samples")] if obj.get("samples") is not None else None
        })
        return _obj


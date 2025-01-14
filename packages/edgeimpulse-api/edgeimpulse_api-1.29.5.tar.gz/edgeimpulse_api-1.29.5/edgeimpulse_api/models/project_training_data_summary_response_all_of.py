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



from pydantic import BaseModel, Field
from edgeimpulse_api.models.project_data_summary import ProjectDataSummary

class ProjectTrainingDataSummaryResponseAllOf(BaseModel):
    data_summary: ProjectDataSummary = Field(..., alias="dataSummary")
    __properties = ["dataSummary"]

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
    def from_json(cls, json_str: str) -> ProjectTrainingDataSummaryResponseAllOf:
        """Create an instance of ProjectTrainingDataSummaryResponseAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data_summary
        if self.data_summary:
            _dict['dataSummary'] = self.data_summary.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectTrainingDataSummaryResponseAllOf:
        """Create an instance of ProjectTrainingDataSummaryResponseAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProjectTrainingDataSummaryResponseAllOf.construct(**obj)

        _obj = ProjectTrainingDataSummaryResponseAllOf.construct(**{
            "data_summary": ProjectDataSummary.from_dict(obj.get("dataSummary")) if obj.get("dataSummary") is not None else None
        })
        return _obj


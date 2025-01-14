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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class OrganizationPipelineStep(BaseModel):
    name: StrictStr = ...
    filter: Optional[StrictStr] = None
    upload_type: Optional[StrictStr] = Field(None, alias="uploadType")
    project_id: Optional[StrictInt] = Field(None, alias="projectId")
    new_project_name: Optional[StrictStr] = Field(None, alias="newProjectName")
    project_api_key: Optional[StrictStr] = Field(None, alias="projectApiKey")
    project_hmac_key: Optional[StrictStr] = Field(None, alias="projectHmacKey")
    transformation_block_id: Optional[StrictInt] = Field(None, alias="transformationBlockId")
    builtin_transformation_block: Optional[Dict[str, Any]] = Field(None, alias="builtinTransformationBlock")
    category: Optional[StrictStr] = None
    output_dataset_name: Optional[StrictStr] = Field(None, alias="outputDatasetName")
    output_dataset_bucket_id: Optional[StrictInt] = Field(None, alias="outputDatasetBucketId")
    output_dataset_bucket_path: Optional[StrictStr] = Field(None, alias="outputDatasetBucketPath")
    label: Optional[StrictStr] = None
    transformation_parallel: Optional[StrictInt] = Field(None, alias="transformationParallel")
    extra_cli_arguments: Optional[StrictStr] = Field(None, alias="extraCliArguments")
    parameters: Optional[Dict[str, StrictStr]] = None
    __properties = ["name", "filter", "uploadType", "projectId", "newProjectName", "projectApiKey", "projectHmacKey", "transformationBlockId", "builtinTransformationBlock", "category", "outputDatasetName", "outputDatasetBucketId", "outputDatasetBucketPath", "label", "transformationParallel", "extraCliArguments", "parameters"]

    @validator('upload_type')
    def upload_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('project', 'dataset'):
            raise ValueError("must validate the enum values ('project', 'dataset')")
        return v

    @validator('category')
    def category_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('training', 'testing', 'split'):
            raise ValueError("must validate the enum values ('training', 'testing', 'split')")
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
    def from_json(cls, json_str: str) -> OrganizationPipelineStep:
        """Create an instance of OrganizationPipelineStep from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationPipelineStep:
        """Create an instance of OrganizationPipelineStep from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrganizationPipelineStep.construct(**obj)

        _obj = OrganizationPipelineStep.construct(**{
            "name": obj.get("name"),
            "filter": obj.get("filter"),
            "upload_type": obj.get("uploadType"),
            "project_id": obj.get("projectId"),
            "new_project_name": obj.get("newProjectName"),
            "project_api_key": obj.get("projectApiKey"),
            "project_hmac_key": obj.get("projectHmacKey"),
            "transformation_block_id": obj.get("transformationBlockId"),
            "builtin_transformation_block": obj.get("builtinTransformationBlock"),
            "category": obj.get("category"),
            "output_dataset_name": obj.get("outputDatasetName"),
            "output_dataset_bucket_id": obj.get("outputDatasetBucketId"),
            "output_dataset_bucket_path": obj.get("outputDatasetBucketPath"),
            "label": obj.get("label"),
            "transformation_parallel": obj.get("transformationParallel"),
            "extra_cli_arguments": obj.get("extraCliArguments"),
            "parameters": obj.get("parameters")
        })
        return _obj


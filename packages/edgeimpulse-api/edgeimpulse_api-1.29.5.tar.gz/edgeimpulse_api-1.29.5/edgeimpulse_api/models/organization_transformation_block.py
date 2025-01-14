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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator
from edgeimpulse_api.models.dsp_group_item import DSPGroupItem
from edgeimpulse_api.models.transformation_block_additional_mount_point import TransformationBlockAdditionalMountPoint

class OrganizationTransformationBlock(BaseModel):
    id: StrictInt = ...
    name: StrictStr = ...
    docker_container: StrictStr = Field(..., alias="dockerContainer")
    docker_container_managed_by_edge_impulse: StrictBool = Field(..., alias="dockerContainerManagedByEdgeImpulse")
    created: datetime = ...
    user_id: Optional[StrictInt] = Field(None, alias="userId")
    user_name: Optional[StrictStr] = Field(None, alias="userName")
    description: StrictStr = ...
    cli_arguments: StrictStr = Field(..., alias="cliArguments", description="These arguments are passed into the container")
    ind_metadata: StrictBool = Field(..., alias="indMetadata")
    requests_cpu: Optional[float] = Field(None, alias="requestsCpu")
    requests_memory: Optional[StrictInt] = Field(None, alias="requestsMemory")
    limits_cpu: Optional[float] = Field(None, alias="limitsCpu")
    limits_memory: Optional[StrictInt] = Field(None, alias="limitsMemory")
    additional_mount_points: List[TransformationBlockAdditionalMountPoint] = Field(..., alias="additionalMountPoints")
    operates_on: StrictStr = Field(..., alias="operatesOn")
    allow_extra_cli_arguments: StrictBool = Field(..., alias="allowExtraCliArguments")
    parameters: Optional[List[Dict[str, Any]]] = Field(None, description="List of parameters, spec'ed according to https://docs.edgeimpulse.com/docs/tips-and-tricks/adding-parameters-to-custom-blocks")
    parameters_ui: Optional[List[DSPGroupItem]] = Field(None, alias="parametersUI", description="List of parameters to be rendered in the UI")
    __properties = ["id", "name", "dockerContainer", "dockerContainerManagedByEdgeImpulse", "created", "userId", "userName", "description", "cliArguments", "indMetadata", "requestsCpu", "requestsMemory", "limitsCpu", "limitsMemory", "additionalMountPoints", "operatesOn", "allowExtraCliArguments", "parameters", "parametersUI"]

    @validator('operates_on')
    def operates_on_validate_enum(cls, v):
        if v not in ('file', 'dataitem', 'standalone'):
            raise ValueError("must validate the enum values ('file', 'dataitem', 'standalone')")
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
    def from_json(cls, json_str: str) -> OrganizationTransformationBlock:
        """Create an instance of OrganizationTransformationBlock from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in additional_mount_points (list)
        _items = []
        if self.additional_mount_points:
            for _item in self.additional_mount_points:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalMountPoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parameters_ui (list)
        _items = []
        if self.parameters_ui:
            for _item in self.parameters_ui:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parametersUI'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationTransformationBlock:
        """Create an instance of OrganizationTransformationBlock from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrganizationTransformationBlock.construct(**obj)

        _obj = OrganizationTransformationBlock.construct(**{
            "id": obj.get("id"),
            "name": obj.get("name"),
            "docker_container": obj.get("dockerContainer"),
            "docker_container_managed_by_edge_impulse": obj.get("dockerContainerManagedByEdgeImpulse"),
            "created": obj.get("created"),
            "user_id": obj.get("userId"),
            "user_name": obj.get("userName"),
            "description": obj.get("description"),
            "cli_arguments": obj.get("cliArguments"),
            "ind_metadata": obj.get("indMetadata"),
            "requests_cpu": obj.get("requestsCpu"),
            "requests_memory": obj.get("requestsMemory"),
            "limits_cpu": obj.get("limitsCpu"),
            "limits_memory": obj.get("limitsMemory"),
            "additional_mount_points": [TransformationBlockAdditionalMountPoint.from_dict(_item) for _item in obj.get("additionalMountPoints")] if obj.get("additionalMountPoints") is not None else None,
            "operates_on": obj.get("operatesOn"),
            "allow_extra_cli_arguments": obj.get("allowExtraCliArguments"),
            "parameters": obj.get("parameters"),
            "parameters_ui": [DSPGroupItem.from_dict(_item) for _item in obj.get("parametersUI")] if obj.get("parametersUI") is not None else None
        })
        return _obj


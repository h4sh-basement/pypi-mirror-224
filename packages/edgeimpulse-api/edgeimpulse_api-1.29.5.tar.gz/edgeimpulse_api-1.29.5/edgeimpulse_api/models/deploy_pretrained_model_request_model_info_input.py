# coding: utf-8

"""
    Edge Impulse API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from edgeimpulse_api.models.deploy_pretrained_model_input_audio import DeployPretrainedModelInputAudio
from edgeimpulse_api.models.deploy_pretrained_model_input_image import DeployPretrainedModelInputImage
from edgeimpulse_api.models.deploy_pretrained_model_input_other import DeployPretrainedModelInputOther
from edgeimpulse_api.models.deploy_pretrained_model_input_time_series import DeployPretrainedModelInputTimeSeries
from typing import Any, List
from pydantic import StrictStr, Field

DEPLOYPRETRAINEDMODELREQUESTMODELINFOINPUT_ONE_OF_SCHEMAS = ["DeployPretrainedModelInputAudio", "DeployPretrainedModelInputImage", "DeployPretrainedModelInputOther", "DeployPretrainedModelInputTimeSeries"]

class DeployPretrainedModelRequestModelInfoInput(BaseModel):
    # data type: DeployPretrainedModelInputTimeSeries
    oneof_schema_1_validator: Optional[DeployPretrainedModelInputTimeSeries] = None
    # data type: DeployPretrainedModelInputAudio
    oneof_schema_2_validator: Optional[DeployPretrainedModelInputAudio] = None
    # data type: DeployPretrainedModelInputImage
    oneof_schema_3_validator: Optional[DeployPretrainedModelInputImage] = None
    # data type: DeployPretrainedModelInputOther
    oneof_schema_4_validator: Optional[DeployPretrainedModelInputOther] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(DEPLOYPRETRAINEDMODELREQUESTMODELINFOINPUT_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = False

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: DeployPretrainedModelInputTimeSeries
        if type(v) is not DeployPretrainedModelInputTimeSeries:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DeployPretrainedModelInputTimeSeries`")
        else:
            match += 1

        # validate data type: DeployPretrainedModelInputAudio
        if type(v) is not DeployPretrainedModelInputAudio:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DeployPretrainedModelInputAudio`")
        else:
            match += 1

        # validate data type: DeployPretrainedModelInputImage
        if type(v) is not DeployPretrainedModelInputImage:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DeployPretrainedModelInputImage`")
        else:
            match += 1

        # validate data type: DeployPretrainedModelInputOther
        if type(v) is not DeployPretrainedModelInputOther:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DeployPretrainedModelInputOther`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into DeployPretrainedModelRequestModelInfoInput with oneOf schemas: DeployPretrainedModelInputAudio, DeployPretrainedModelInputImage, DeployPretrainedModelInputOther, DeployPretrainedModelInputTimeSeries. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DeployPretrainedModelRequestModelInfoInput with oneOf schemas: DeployPretrainedModelInputAudio, DeployPretrainedModelInputImage, DeployPretrainedModelInputOther, DeployPretrainedModelInputTimeSeries. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> DeployPretrainedModelRequestModelInfoInput:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> DeployPretrainedModelRequestModelInfoInput:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        if "DeployPretrainedModelRequestModelInfoInput" == 'TestPretrainedModelRequestModelInfoInput':
            temp = DeployPretrainedModelInputOther.from_json(json_str)
            if temp.input_type == 'time-series':
                instance.actual_instance = DeployPretrainedModelInputTimeSeries.from_json(json_str)
                match = 1
            elif temp.input_type == 'image':
                instance.actual_instance = DeployPretrainedModelInputImage.from_json(json_str)
                match = 1
            elif temp.input_type == 'audio':
                instance.actual_instance = DeployPretrainedModelInputAudio.from_json(json_str)
                match = 1
            elif temp.input_type == 'other':
                instance.actual_instance = DeployPretrainedModelInputOther.from_json(json_str)
                match = 1
            else:
                raise "Unknown model input"
        elif "DeployPretrainedModelRequestModelInfoInput" == 'DeployPretrainedModelRequestModelInfoModel':
            temp = DeployPretrainedModelModelClassification.from_json(json_str)
            if temp.model_type == 'classification':
                instance.actual_instance = DeployPretrainedModelModelClassification.from_json(json_str)
                match = 1
            elif temp.model_type == 'regression':
                instance.actual_instance = DeployPretrainedModelModelRegression.from_json(json_str)
                match = 1
            elif temp.model_type == 'object-detection':
                instance.actual_instance = DeployPretrainedModelModelObjectDetection.from_json(json_str)
                match = 1
            else:
                raise "Unknown model type"
        elif "DeployPretrainedModelRequestModelInfoInput" == 'DeployPretrainedModelRequestModelInfoInput':
            temp = DeployPretrainedModelInputOther.from_json(json_str)
            if temp.input_type == 'time-series':
                instance.actual_instance = DeployPretrainedModelInputTimeSeries.from_json(json_str)
                match = 1
            elif temp.input_type == 'image':
                instance.actual_instance = DeployPretrainedModelInputImage.from_json(json_str)
                match = 1
            elif temp.input_type == 'audio':
                instance.actual_instance = DeployPretrainedModelInputAudio.from_json(json_str)
                match = 1
            elif temp.input_type == 'other':
                instance.actual_instance = DeployPretrainedModelInputOther.from_json(json_str)
                match = 1
            else:
                raise "Unknown model input"
        else:
            raise "No class implemented for oneof"


        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into DeployPretrainedModelRequestModelInfoInput with oneOf schemas: DeployPretrainedModelInputAudio, DeployPretrainedModelInputImage, DeployPretrainedModelInputOther, DeployPretrainedModelInputTimeSeries. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DeployPretrainedModelRequestModelInfoInput with oneOf schemas: DeployPretrainedModelInputAudio, DeployPretrainedModelInputImage, DeployPretrainedModelInputOther, DeployPretrainedModelInputTimeSeries. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.178.1
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt

class LongTermOfferedCapacity(BaseModel):
    """
    LongTermOfferedCapacity
    """
    preliminary_oc: StrictInt = Field(..., alias="preliminaryOc", description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    returned_oc: Optional[StrictInt] = Field(None, alias="returnedOc", description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    final_oc: StrictInt = Field(..., alias="finalOc", description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    __properties = ["preliminaryOc", "returnedOc", "finalOc"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LongTermOfferedCapacity:
        """Create an instance of LongTermOfferedCapacity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LongTermOfferedCapacity:
        """Create an instance of LongTermOfferedCapacity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LongTermOfferedCapacity.parse_obj(obj)

        _obj = LongTermOfferedCapacity.parse_obj({
            "preliminary_oc": obj.get("preliminaryOc"),
            "returned_oc": obj.get("returnedOc"),
            "final_oc": obj.get("finalOc")
        })
        return _obj


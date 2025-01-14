# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.176.7
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, constr, validator
from empire_platform_api_public_client.models.default_nomination_declaration_type import DefaultNominationDeclarationType

class DefaultNominationMtu(BaseModel):
    """
    DefaultNominationMtu
    """
    mtu: constr(strict=True) = Field(..., description="The first moment (inclusive) of an MTU period in local time, minute resolution, interpreted in **System Time**  - string, interpreted in `hh:mm` format - only `XX:00`, `XX:15`, `XX:30` and `XX:45` are valid values (depending on MTU size) ")
    type: DefaultNominationDeclarationType = Field(...)
    value: Optional[StrictInt] = Field(None, description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    __properties = ["mtu", "type", "value"]

    # @validator('mtu')
    def mtu_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0[0-9]|1[0-9]|2[0-3]):(00|15|30|45)$", value):
            raise ValueError(r"must validate the regular expression /^(0[0-9]|1[0-9]|2[0-3]):(00|15|30|45)$/")
        return value

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
    def from_json(cls, json_str: str) -> DefaultNominationMtu:
        """Create an instance of DefaultNominationMtu from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DefaultNominationMtu:
        """Create an instance of DefaultNominationMtu from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DefaultNominationMtu.parse_obj(obj)

        _obj = DefaultNominationMtu.parse_obj({
            "mtu": obj.get("mtu"),
            "type": obj.get("type"),
            "value": obj.get("value")
        })
        return _obj


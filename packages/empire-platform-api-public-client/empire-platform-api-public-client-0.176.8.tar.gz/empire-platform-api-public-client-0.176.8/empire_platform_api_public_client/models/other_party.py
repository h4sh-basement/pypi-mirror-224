# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.176.8
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class OtherParty(BaseModel):
    """
    Participant basic information
    """
    id: StrictStr = Field(..., description="Unique identifier for the record in UUID4 format")
    name: StrictStr = Field(...)
    __properties = ["id", "name"]

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
    def from_json(cls, json_str: str) -> OtherParty:
        """Create an instance of OtherParty from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OtherParty:
        """Create an instance of OtherParty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OtherParty.parse_obj(obj)

        _obj = OtherParty.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


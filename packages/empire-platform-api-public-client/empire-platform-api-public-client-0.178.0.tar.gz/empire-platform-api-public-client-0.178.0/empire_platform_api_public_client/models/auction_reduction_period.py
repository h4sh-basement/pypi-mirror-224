# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.178.0
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt
from empire_platform_api_public_client.models.date_time_period import DateTimePeriod

class AuctionReductionPeriod(BaseModel):
    """
    AuctionReductionPeriod
    """
    period: DateTimePeriod = Field(...)
    atc_reduction: StrictInt = Field(..., alias="atcReduction", description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    available_atc: StrictInt = Field(..., alias="availableAtc", description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    __properties = ["period", "atcReduction", "availableAtc"]

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
    def from_json(cls, json_str: str) -> AuctionReductionPeriod:
        """Create an instance of AuctionReductionPeriod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of period
        if self.period:
            _dict['period'] = self.period.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuctionReductionPeriod:
        """Create an instance of AuctionReductionPeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuctionReductionPeriod.parse_obj(obj)

        _obj = AuctionReductionPeriod.parse_obj({
            "period": DateTimePeriod.from_dict(obj.get("period")) if obj.get("period") is not None else None,
            "atc_reduction": obj.get("atcReduction"),
            "available_atc": obj.get("availableAtc")
        })
        return _obj


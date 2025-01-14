# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.176.3
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, conlist
from empire_platform_api_public_client.models.aggregated_nominations_mtu_netted_nominations import AggregatedNominationsMtuNettedNominations
from empire_platform_api_public_client.models.aggregated_nominations_mtu_value import AggregatedNominationsMtuValue
from empire_platform_api_public_client.models.aggregated_nominations_nl_mtus_inner_eprogram_values import AggregatedNominationsNlMtusInnerEprogramValues

class AggregatedNominationsNlMtusInner(BaseModel):
    """
    AggregatedNominationsNlMtusInner
    """
    mtu: datetime = Field(..., description="The first moment (inclusive) of an MTU period  - theoretically can be sent and received with any zone offset (until it marks the desired **absolute MTU start point** on the timeline) - in practice it is advised to transfer it in UTC timezone (with Z offset, \"Zulu time\") - ISO 8601 compliant string in `yyyy-mm-ddThh:mm:ss.SSSZ` format - only with `XX:00:00`, `XX:15:00`, `XX:30:00` and `XX:45:00` time parts are valid values (depending on MTU size) ")
    values: conlist(AggregatedNominationsMtuValue) = Field(...)
    netted_nominations: AggregatedNominationsMtuNettedNominations = Field(..., alias="nettedNominations")
    eprogram_values: AggregatedNominationsNlMtusInnerEprogramValues = Field(..., alias="eprogramValues")
    __properties = ["mtu", "values", "nettedNominations", "eprogramValues"]

    # @validator('mtu')
    def mtu_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.*T.*:(00|15|30|45):00(\.0+)?(Z|\+.*)$", value):
            raise ValueError(r"must validate the regular expression /^.*T.*:(00|15|30|45):00(\.0+)?(Z|\+.*)$/")
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
    def from_json(cls, json_str: str) -> AggregatedNominationsNlMtusInner:
        """Create an instance of AggregatedNominationsNlMtusInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        # override the default output from pydantic by calling `to_dict()` of netted_nominations
        if self.netted_nominations:
            _dict['nettedNominations'] = self.netted_nominations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eprogram_values
        if self.eprogram_values:
            _dict['eprogramValues'] = self.eprogram_values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AggregatedNominationsNlMtusInner:
        """Create an instance of AggregatedNominationsNlMtusInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AggregatedNominationsNlMtusInner.parse_obj(obj)

        _obj = AggregatedNominationsNlMtusInner.parse_obj({
            "mtu": obj.get("mtu"),
            "values": [AggregatedNominationsMtuValue.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None,
            "netted_nominations": AggregatedNominationsMtuNettedNominations.from_dict(obj.get("nettedNominations")) if obj.get("nettedNominations") is not None else None,
            "eprogram_values": AggregatedNominationsNlMtusInnerEprogramValues.from_dict(obj.get("eprogramValues")) if obj.get("eprogramValues") is not None else None
        })
        return _obj


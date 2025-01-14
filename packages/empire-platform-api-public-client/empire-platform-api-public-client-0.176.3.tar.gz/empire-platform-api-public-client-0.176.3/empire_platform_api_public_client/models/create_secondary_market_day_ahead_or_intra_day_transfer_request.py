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

from datetime import date
from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from empire_platform_api_public_client.models.auction_timescale import AuctionTimescale
from empire_platform_api_public_client.models.border_direction import BorderDirection
from empire_platform_api_public_client.models.create_secondary_market_day_ahead_or_intra_day_transfer_request_mtus_inner import CreateSecondaryMarketDayAheadOrIntraDayTransferRequestMtusInner

class CreateSecondaryMarketDayAheadOrIntraDayTransferRequest(BaseModel):
    """
    CreateSecondaryMarketDayAheadOrIntraDayTransferRequest
    """
    delivery_day: date = Field(..., alias="deliveryDay", description="One single calendar day, interpreted in **System Time**  - ISO 8601 compliant string in `yyyy-mm-dd` format ")
    direction: BorderDirection = Field(...)
    participant_id: StrictStr = Field(..., alias="participantId", description="Unique identifier for the record in UUID4 format")
    timescale: AuctionTimescale = Field(...)
    mtus: conlist(CreateSecondaryMarketDayAheadOrIntraDayTransferRequestMtusInner) = Field(...)
    __properties = ["deliveryDay", "direction", "participantId", "timescale", "mtus"]

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
    def from_json(cls, json_str: str) -> CreateSecondaryMarketDayAheadOrIntraDayTransferRequest:
        """Create an instance of CreateSecondaryMarketDayAheadOrIntraDayTransferRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in mtus (list)
        _items = []
        if self.mtus:
            for _item in self.mtus:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mtus'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSecondaryMarketDayAheadOrIntraDayTransferRequest:
        """Create an instance of CreateSecondaryMarketDayAheadOrIntraDayTransferRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSecondaryMarketDayAheadOrIntraDayTransferRequest.parse_obj(obj)

        _obj = CreateSecondaryMarketDayAheadOrIntraDayTransferRequest.parse_obj({
            "delivery_day": obj.get("deliveryDay"),
            "direction": obj.get("direction"),
            "participant_id": obj.get("participantId"),
            "timescale": obj.get("timescale"),
            "mtus": [CreateSecondaryMarketDayAheadOrIntraDayTransferRequestMtusInner.from_dict(_item) for _item in obj.get("mtus")] if obj.get("mtus") is not None else None
        })
        return _obj


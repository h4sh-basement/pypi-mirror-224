# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.179.2
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, confloat, conint, conlist
from empire_platform_api_public_client.models.auction_result_congestion_rent import AuctionResultCongestionRent
from empire_platform_api_public_client.models.day_ahead_or_intra_day_auction_mtu_results_bids_inner import DayAheadOrIntraDayAuctionMtuResultsBidsInner
from empire_platform_api_public_client.models.long_term_auction_results_allocated_capacity_inner import LongTermAuctionResultsAllocatedCapacityInner

class LongTermAuctionResults(BaseModel):
    """
    LongTermAuctionResults
    """
    congestion_rent: Optional[AuctionResultCongestionRent] = Field(None, alias="congestionRent")
    bids: conlist(DayAheadOrIntraDayAuctionMtuResultsBidsInner) = Field(...)
    allocated_capacity: conlist(LongTermAuctionResultsAllocatedCapacityInner) = Field(..., alias="allocatedCapacity")
    marginal_price: Union[confloat(multiple_of=0.01, strict=True), conint(strict=True)] = Field(..., alias="marginalPrice", description="Currency value in Euros (€), accepted with a precision of maximum 2 decimal places")
    reserve_price: Optional[Union[confloat(multiple_of=0.01, strict=True), conint(strict=True)]] = Field(None, alias="reservePrice", description="Currency value in Euros (€), accepted with a precision of maximum 2 decimal places")
    __properties = ["congestionRent", "bids", "allocatedCapacity", "marginalPrice", "reservePrice"]

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
    def from_json(cls, json_str: str) -> LongTermAuctionResults:
        """Create an instance of LongTermAuctionResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of congestion_rent
        if self.congestion_rent:
            _dict['congestionRent'] = self.congestion_rent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in bids (list)
        _items = []
        if self.bids:
            for _item in self.bids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bids'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in allocated_capacity (list)
        _items = []
        if self.allocated_capacity:
            for _item in self.allocated_capacity:
                if _item:
                    _items.append(_item.to_dict())
            _dict['allocatedCapacity'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LongTermAuctionResults:
        """Create an instance of LongTermAuctionResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LongTermAuctionResults.parse_obj(obj)

        _obj = LongTermAuctionResults.parse_obj({
            "congestion_rent": AuctionResultCongestionRent.from_dict(obj.get("congestionRent")) if obj.get("congestionRent") is not None else None,
            "bids": [DayAheadOrIntraDayAuctionMtuResultsBidsInner.from_dict(_item) for _item in obj.get("bids")] if obj.get("bids") is not None else None,
            "allocated_capacity": [LongTermAuctionResultsAllocatedCapacityInner.from_dict(_item) for _item in obj.get("allocatedCapacity")] if obj.get("allocatedCapacity") is not None else None,
            "marginal_price": obj.get("marginalPrice"),
            "reserve_price": obj.get("reservePrice")
        })
        return _obj


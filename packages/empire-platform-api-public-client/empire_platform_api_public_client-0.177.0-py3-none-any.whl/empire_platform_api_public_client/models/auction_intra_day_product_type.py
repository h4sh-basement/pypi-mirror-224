# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.177.0
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class AuctionIntraDayProductType(str, Enum):
    """
    AuctionIntraDayProductType
    """

    """
    allowed enum values
    """
    ID_EXPLICIT_ID_1 = 'ID_EXPLICIT_ID_1'
    ID_EXPLICIT_ID_2 = 'ID_EXPLICIT_ID_2'
    ID_EXPLICIT_ID_3 = 'ID_EXPLICIT_ID_3'
    ID_EXPLICIT_ID_4 = 'ID_EXPLICIT_ID_4'

    @classmethod
    def from_json(cls, json_str: str) -> AuctionIntraDayProductType:
        """Create an instance of AuctionIntraDayProductType from a JSON string"""
        return AuctionIntraDayProductType(json.loads(json_str))



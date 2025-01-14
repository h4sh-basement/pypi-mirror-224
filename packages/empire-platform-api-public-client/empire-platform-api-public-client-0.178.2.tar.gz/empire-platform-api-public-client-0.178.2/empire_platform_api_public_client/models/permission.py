# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.178.2
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Permission(str, Enum):
    """
    Permission
    """

    """
    allowed enum values
    """
    VIEW_PUBLISHED_AUCTIONS = 'VIEW_PUBLISHED_AUCTIONS'
    VIEW_ANY_AUCTIONS = 'VIEW_ANY_AUCTIONS'
    MANAGE_AUCTIONS = 'MANAGE_AUCTIONS'
    VIEW_AUCTION_BIDS = 'VIEW_AUCTION_BIDS'
    MANAGE_LT_AUCTION_BIDS = 'MANAGE_LT_AUCTION_BIDS'
    MANAGE_DA_ID_AUCTION_BIDS = 'MANAGE_DA_ID_AUCTION_BIDS'
    VIEW_AUCTION_DEFAULTS = 'VIEW_AUCTION_DEFAULTS'
    MANAGE_AUCTION_DEFAULTS = 'MANAGE_AUCTION_DEFAULTS'
    VIEW_CAPACITY_OVERVIEW = 'VIEW_CAPACITY_OVERVIEW'
    VIEW_NTC_OVERVIEW = 'VIEW_NTC_OVERVIEW'
    SUBMIT_NTC_OVERRIDE = 'SUBMIT_NTC_OVERRIDE'
    VIEW_NTC_REDUCTIONS = 'VIEW_NTC_REDUCTIONS'
    MANAGE_NTC_REDUCTIONS = 'MANAGE_NTC_REDUCTIONS'
    VIEW_NTC_ADDITIONS = 'VIEW_NTC_ADDITIONS'
    MANAGE_NTC_ADDITIONS = 'MANAGE_NTC_ADDITIONS'
    VIEW_UNPLANNED_OUTAGES = 'VIEW_UNPLANNED_OUTAGES'
    MANAGE_UNPLANNED_OUTAGES = 'MANAGE_UNPLANNED_OUTAGES'
    VIEW_PLANNED_OUTAGES = 'VIEW_PLANNED_OUTAGES'
    MANAGE_PLANNED_OUTAGES = 'MANAGE_PLANNED_OUTAGES'
    VIEW_OWN_TRANSMISSION_RIGHTS = 'VIEW_OWN_TRANSMISSION_RIGHTS'
    VIEW_ANY_TRANSMISSION_RIGHTS = 'VIEW_ANY_TRANSMISSION_RIGHTS'
    VIEW_OWN_TIMESCALE_NOMINATIONS = 'VIEW_OWN_TIMESCALE_NOMINATIONS'
    MANAGE_OWN_TIMESCALE_NOMINATIONS = 'MANAGE_OWN_TIMESCALE_NOMINATIONS'
    VIEW_ANY_TIMESCALE_NOMINATIONS = 'VIEW_ANY_TIMESCALE_NOMINATIONS'
    MANAGE_ANY_TIMESCALE_NOMINATIONS = 'MANAGE_ANY_TIMESCALE_NOMINATIONS'
    VIEW_SOSO_NOMINATIONS = 'VIEW_SOSO_NOMINATIONS'
    MANAGE_SOSO_NOMINATIONS = 'MANAGE_SOSO_NOMINATIONS'
    VIEW_BPP_NOMINATIONS = 'VIEW_BPP_NOMINATIONS'
    MANAGE_BPP_NOMINATIONS = 'MANAGE_BPP_NOMINATIONS'
    VIEW_OWN_TIMESCALE_OR_BPP_AGGREGATED_NOMINATIONS = 'VIEW_OWN_TIMESCALE_OR_BPP_AGGREGATED_NOMINATIONS'
    VIEW_ANY_TIMESCALE_OR_BPP_AGGREGATED_NOMINATIONS = 'VIEW_ANY_TIMESCALE_OR_BPP_AGGREGATED_NOMINATIONS'
    VIEW_SOSO_AGGREGATED_NOMINATIONS = 'VIEW_SOSO_AGGREGATED_NOMINATIONS'
    VIEW_OWN_DEFAULT_BIDS = 'VIEW_OWN_DEFAULT_BIDS'
    MANAGE_OWN_DEFAULT_BIDS = 'MANAGE_OWN_DEFAULT_BIDS'
    VIEW_ANY_DEFAULT_BIDS = 'VIEW_ANY_DEFAULT_BIDS'
    MANAGE_ANY_DEFAULT_BIDS = 'MANAGE_ANY_DEFAULT_BIDS'
    VIEW_OWN_DEFAULT_NOMINATIONS = 'VIEW_OWN_DEFAULT_NOMINATIONS'
    MANAGE_OWN_DEFAULT_NOMINATIONS = 'MANAGE_OWN_DEFAULT_NOMINATIONS'
    VIEW_ANY_DEFAULT_NOMINATIONS = 'VIEW_ANY_DEFAULT_NOMINATIONS'
    MANAGE_ANY_DEFAULT_NOMINATIONS = 'MANAGE_ANY_DEFAULT_NOMINATIONS'
    VIEW_NOM_WINDOW_OVERRIDES = 'VIEW_NOM_WINDOW_OVERRIDES'
    MANAGE_NOM_WINDOW_OVERRIDES = 'MANAGE_NOM_WINDOW_OVERRIDES'
    VIEW_CRISIS = 'VIEW_CRISIS'
    MANAGE_CRISIS_ACTIONS = 'MANAGE_CRISIS_ACTIONS'
    MANAGE_CRISIS_MESSAGES = 'MANAGE_CRISIS_MESSAGES'
    VIEW_ANY_ORGANISATIONS = 'VIEW_ANY_ORGANISATIONS'
    MANAGE_ANY_ORGANISATIONS = 'MANAGE_ANY_ORGANISATIONS'
    VIEW_OWN_ORGANISATIONS = 'VIEW_OWN_ORGANISATIONS'
    VIEW_OWN_USERS = 'VIEW_OWN_USERS'
    VIEW_ANY_USERS = 'VIEW_ANY_USERS'
    MANAGE_OWN_USERS = 'MANAGE_OWN_USERS'
    MANAGE_ANY_USERS = 'MANAGE_ANY_USERS'
    INVITE_USERS = 'INVITE_USERS'
    IMPERSONATE_USERS = 'IMPERSONATE_USERS'
    VIEW_ICO_DASHBOARD = 'VIEW_ICO_DASHBOARD'
    VIEW_PARTICIPANT_DASHBOARD = 'VIEW_PARTICIPANT_DASHBOARD'
    VIEW_GENERAL_SYSTEM_MESSAGES = 'VIEW_GENERAL_SYSTEM_MESSAGES'
    VIEW_OPERATIONAL_SYSTEM_MESSAGES = 'VIEW_OPERATIONAL_SYSTEM_MESSAGES'
    VIEW_PARTICIPANT_MESSAGES = 'VIEW_PARTICIPANT_MESSAGES'
    VIEW_BUSINESS_SETTINGS = 'VIEW_BUSINESS_SETTINGS'
    MANAGE_BUSINESS_SETTINGS = 'MANAGE_BUSINESS_SETTINGS'
    VIEW_PROTECTED_CONFIG_VARIABLES = 'VIEW_PROTECTED_CONFIG_VARIABLES'
    VIEW_OWN_BIDDING_CONFIGURATION = 'VIEW_OWN_BIDDING_CONFIGURATION'
    MANAGE_OWN_BIDDING_CONFIGURATION = 'MANAGE_OWN_BIDDING_CONFIGURATION'
    VIEW_ANY_BIDDING_CONFIGURATION = 'VIEW_ANY_BIDDING_CONFIGURATION'
    MANAGE_ANY_BIDDING_CONFIGURATION = 'MANAGE_ANY_BIDDING_CONFIGURATION'
    VIEW_OWN_ORGANISATION_DOCUMENTS = 'VIEW_OWN_ORGANISATION_DOCUMENTS'
    MANAGE_OWN_ORGANISATION_DOCUMENTS = 'MANAGE_OWN_ORGANISATION_DOCUMENTS'
    VIEW_ANY_ORGANISATION_DOCUMENTS = 'VIEW_ANY_ORGANISATION_DOCUMENTS'
    MANAGE_ANY_ORGANISATION_DOCUMENTS = 'MANAGE_ANY_ORGANISATION_DOCUMENTS'
    VIEW_BPP = 'VIEW_BPP'
    MANAGE_BPP = 'MANAGE_BPP'
    VIEW_ANY_BUY_NOW_OFFERS = 'VIEW_ANY_BUY_NOW_OFFERS'
    VIEW_OWN_BUY_NOW_OFFERS = 'VIEW_OWN_BUY_NOW_OFFERS'
    MANAGE_BUY_NOW_OFFERS = 'MANAGE_BUY_NOW_OFFERS'
    PURCHASE_BUY_NOW_OFFERS = 'PURCHASE_BUY_NOW_OFFERS'
    VIEW_ANY_SECONDARY_MARKET_RETURNS = 'VIEW_ANY_SECONDARY_MARKET_RETURNS'
    VIEW_OWN_SECONDARY_MARKET_RETURNS = 'VIEW_OWN_SECONDARY_MARKET_RETURNS'
    MANAGE_SECONDARY_MARKET_RETURNS = 'MANAGE_SECONDARY_MARKET_RETURNS'
    VIEW_ANY_SECONDARY_MARKET_TRANSFERS = 'VIEW_ANY_SECONDARY_MARKET_TRANSFERS'
    VIEW_OWN_SECONDARY_MARKET_TRANSFERS = 'VIEW_OWN_SECONDARY_MARKET_TRANSFERS'
    MANAGE_SECONDARY_MARKET_LT_TRANSFERS = 'MANAGE_SECONDARY_MARKET_LT_TRANSFERS'
    MANAGE_SECONDARY_MARKET_DA_ID_TRANSFERS = 'MANAGE_SECONDARY_MARKET_DA_ID_TRANSFERS'
    VIEW_BUSINESS_PROCESSES = 'VIEW_BUSINESS_PROCESSES'
    MANAGE_BUSINESS_PROCESSES = 'MANAGE_BUSINESS_PROCESSES'
    VIEW_DATA_FLOWS = 'VIEW_DATA_FLOWS'
    MANAGE_DATA_FLOWS = 'MANAGE_DATA_FLOWS'
    MANAGE_OWN_MANUAL_FILE_UPLOAD_BIDS = 'MANAGE_OWN_MANUAL_FILE_UPLOAD_BIDS'
    MANAGE_OWN_MANUAL_FILE_UPLOAD_NOMINATIONS = 'MANAGE_OWN_MANUAL_FILE_UPLOAD_NOMINATIONS'
    MANAGE_ANY_MANUAL_FILE_UPLOAD = 'MANAGE_ANY_MANUAL_FILE_UPLOAD'
    VIEW_OWN_AUDIT_LOGS = 'VIEW_OWN_AUDIT_LOGS'
    VIEW_ANY_AUDIT_LOGS = 'VIEW_ANY_AUDIT_LOGS'
    VIEW_ANY_FINANCE_REPORTS = 'VIEW_ANY_FINANCE_REPORTS'
    VIEW_OWN_FINANCE_REPORTS = 'VIEW_OWN_FINANCE_REPORTS'
    VIEW_OWN_SETTLEMENT = 'VIEW_OWN_SETTLEMENT'
    VIEW_ANY_SETTLEMENT = 'VIEW_ANY_SETTLEMENT'
    VIEW_OWN_INVOICES = 'VIEW_OWN_INVOICES'
    VIEW_ANY_INVOICES = 'VIEW_ANY_INVOICES'
    MANAGE_INVOICES = 'MANAGE_INVOICES'
    VIEW_OWN_UIOSI = 'VIEW_OWN_UIOSI'
    VIEW_ANY_UIOSI = 'VIEW_ANY_UIOSI'
    VIEW_CREDIT_OVERVIEW = 'VIEW_CREDIT_OVERVIEW'
    VIEW_HELP_FAQ = 'VIEW_HELP_FAQ'

    @classmethod
    def from_json(cls, json_str: str) -> Permission:
        """Create an instance of Permission from a JSON string"""
        return Permission(json.loads(json_str))



# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.179.2
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import empire_platform_api_public_client
from empire_platform_api_public_client.api.participant_dashboard_api import ParticipantDashboardApi  # noqa: E501
from empire_platform_api_public_client.rest import ApiException


class TestParticipantDashboardApi(unittest.TestCase):
    """ParticipantDashboardApi unit test stubs"""

    def setUp(self):
        self.api = empire_platform_api_public_client.api.participant_dashboard_api.ParticipantDashboardApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_participant_dashboard_default_bids_and_nominations(self):
        """Test case for get_participant_dashboard_default_bids_and_nominations

        """
        pass

    def test_get_participant_dashboard_finance_overview(self):
        """Test case for get_participant_dashboard_finance_overview

        """
        pass

    def test_get_participant_dashboard_interconnector_capacity(self):
        """Test case for get_participant_dashboard_interconnector_capacity

        """
        pass

    def test_get_participant_dashboard_interconnector_capacity_graph(self):
        """Test case for get_participant_dashboard_interconnector_capacity_graph

        """
        pass

    def test_get_participant_dashboard_messages(self):
        """Test case for get_participant_dashboard_messages

        """
        pass

    def test_get_participant_dashboard_netted_nominations(self):
        """Test case for get_participant_dashboard_netted_nominations

        """
        pass

    def test_get_participant_dashboard_next_auctions_and_nomination_gates(self):
        """Test case for get_participant_dashboard_next_auctions_and_nomination_gates

        """
        pass

    def test_get_participant_dashboard_transmission_rights_and_nominations(self):
        """Test case for get_participant_dashboard_transmission_rights_and_nominations

        """
        pass

    def test_get_participant_dashboard_transmission_rights_and_nominations_graph(self):
        """Test case for get_participant_dashboard_transmission_rights_and_nominations_graph

        """
        pass

    def test_get_participant_dashboard_upcoming_long_term_auctions(self):
        """Test case for get_participant_dashboard_upcoming_long_term_auctions

        """
        pass


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.178.2
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import empire_platform_api_public_client
from empire_platform_api_public_client.models.participant_dashboard_interconnector_capacity_graph_data_mtus_inner import ParticipantDashboardInterconnectorCapacityGraphDataMtusInner  # noqa: E501
from empire_platform_api_public_client.rest import ApiException

class TestParticipantDashboardInterconnectorCapacityGraphDataMtusInner(unittest.TestCase):
    """ParticipantDashboardInterconnectorCapacityGraphDataMtusInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParticipantDashboardInterconnectorCapacityGraphDataMtusInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParticipantDashboardInterconnectorCapacityGraphDataMtusInner`
        """
        model = empire_platform_api_public_client.models.participant_dashboard_interconnector_capacity_graph_data_mtus_inner.ParticipantDashboardInterconnectorCapacityGraphDataMtusInner()  # noqa: E501
        if include_optional :
            return ParticipantDashboardInterconnectorCapacityGraphDataMtusInner(
                mtu = '2022-01-04T10:00Z', 
                values = [
                    empire_platform_api_public_client.models.participant_dashboard_interconnector_capacity_graph_data_mtus_inner_values_inner.ParticipantDashboardInterconnectorCapacityGraphData_mtus_inner_values_inner(
                        direction = 'GB_NL', 
                        ntc = 56, )
                    ], 
                netted_nominations = empire_platform_api_public_client.models.participant_dashboard_interconnector_capacity_graph_data_mtus_inner_netted_nominations.ParticipantDashboardInterconnectorCapacityGraphData_mtus_inner_nettedNominations(
                    direction = 'GB_NL', 
                    flow = 56, )
            )
        else :
            return ParticipantDashboardInterconnectorCapacityGraphDataMtusInner(
                mtu = '2022-01-04T10:00Z',
                values = [
                    empire_platform_api_public_client.models.participant_dashboard_interconnector_capacity_graph_data_mtus_inner_values_inner.ParticipantDashboardInterconnectorCapacityGraphData_mtus_inner_values_inner(
                        direction = 'GB_NL', 
                        ntc = 56, )
                    ],
                netted_nominations = empire_platform_api_public_client.models.participant_dashboard_interconnector_capacity_graph_data_mtus_inner_netted_nominations.ParticipantDashboardInterconnectorCapacityGraphData_mtus_inner_nettedNominations(
                    direction = 'GB_NL', 
                    flow = 56, ),
        )
        """

    def testParticipantDashboardInterconnectorCapacityGraphDataMtusInner(self):
        """Test ParticipantDashboardInterconnectorCapacityGraphDataMtusInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

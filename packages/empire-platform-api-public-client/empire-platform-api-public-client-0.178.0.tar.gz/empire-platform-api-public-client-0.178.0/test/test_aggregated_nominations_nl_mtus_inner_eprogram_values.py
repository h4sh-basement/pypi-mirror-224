# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.178.0
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import empire_platform_api_public_client
from empire_platform_api_public_client.models.aggregated_nominations_nl_mtus_inner_eprogram_values import AggregatedNominationsNlMtusInnerEprogramValues  # noqa: E501
from empire_platform_api_public_client.rest import ApiException

class TestAggregatedNominationsNlMtusInnerEprogramValues(unittest.TestCase):
    """AggregatedNominationsNlMtusInnerEprogramValues unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AggregatedNominationsNlMtusInnerEprogramValues
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregatedNominationsNlMtusInnerEprogramValues`
        """
        model = empire_platform_api_public_client.models.aggregated_nominations_nl_mtus_inner_eprogram_values.AggregatedNominationsNlMtusInnerEprogramValues()  # noqa: E501
        if include_optional :
            return AggregatedNominationsNlMtusInnerEprogramValues(
                participant = 56, 
                system = 56
            )
        else :
            return AggregatedNominationsNlMtusInnerEprogramValues(
                participant = 56,
                system = 56,
        )
        """

    def testAggregatedNominationsNlMtusInnerEprogramValues(self):
        """Test AggregatedNominationsNlMtusInnerEprogramValues"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

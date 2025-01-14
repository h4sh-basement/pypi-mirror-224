# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.177.0
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import empire_platform_api_public_client
from empire_platform_api_public_client.api.profile_api import ProfileApi  # noqa: E501
from empire_platform_api_public_client.rest import ApiException


class TestProfileApi(unittest.TestCase):
    """ProfileApi unit test stubs"""

    def setUp(self):
        self.api = empire_platform_api_public_client.api.profile_api.ProfileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api_key(self):
        """Test case for create_api_key

        """
        pass

    def test_delete_api_key(self):
        """Test case for delete_api_key

        """
        pass

    def test_get_api_keys(self):
        """Test case for get_api_keys

        """
        pass

    def test_get_preferences(self):
        """Test case for get_preferences

        """
        pass

    def test_get_profile(self):
        """Test case for get_profile

        """
        pass

    def test_get_profile_details(self):
        """Test case for get_profile_details

        """
        pass

    def test_get_zendesk_chat_token(self):
        """Test case for get_zendesk_chat_token

        """
        pass

    def test_update_preferences(self):
        """Test case for update_preferences

        """
        pass

    def test_update_profile_details(self):
        """Test case for update_profile_details

        """
        pass


if __name__ == '__main__':
    unittest.main()

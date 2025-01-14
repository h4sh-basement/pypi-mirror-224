# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.178.1
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import empire_platform_api_public_client
from empire_platform_api_public_client.models.user_preferences import UserPreferences  # noqa: E501
from empire_platform_api_public_client.rest import ApiException

class TestUserPreferences(unittest.TestCase):
    """UserPreferences unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserPreferences
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserPreferences`
        """
        model = empire_platform_api_public_client.models.user_preferences.UserPreferences()  # noqa: E501
        if include_optional :
            return UserPreferences(
                general_notifications = empire_platform_api_public_client.models.user_preferences_general_notifications.UserPreferences_generalNotifications(
                    critical_alert = empire_platform_api_public_client.models.notification_preference_with_sms.NotificationPreferenceWithSms(
                        email = True, 
                        sms = True, ), 
                    critical = empire_platform_api_public_client.models.notification_preference.NotificationPreference(
                        email = True, ), 
                    major = empire_platform_api_public_client.models.notification_preference.NotificationPreference(
                        email = True, ), 
                    normal = , ), 
                subscription_notifications = empire_platform_api_public_client.models.user_preferences_subscription_notifications.UserPreferences_subscriptionNotifications(
                    long_term_auction_updates = empire_platform_api_public_client.models.notification_preference.NotificationPreference(
                        email = True, ), 
                    buy_now_transmission_rights_offers = empire_platform_api_public_client.models.notification_preference.NotificationPreference(
                        email = True, ), ), 
                appearance = 'DEFAULT'
            )
        else :
            return UserPreferences(
                general_notifications = empire_platform_api_public_client.models.user_preferences_general_notifications.UserPreferences_generalNotifications(
                    critical_alert = empire_platform_api_public_client.models.notification_preference_with_sms.NotificationPreferenceWithSms(
                        email = True, 
                        sms = True, ), 
                    critical = empire_platform_api_public_client.models.notification_preference.NotificationPreference(
                        email = True, ), 
                    major = empire_platform_api_public_client.models.notification_preference.NotificationPreference(
                        email = True, ), 
                    normal = , ),
                subscription_notifications = empire_platform_api_public_client.models.user_preferences_subscription_notifications.UserPreferences_subscriptionNotifications(
                    long_term_auction_updates = empire_platform_api_public_client.models.notification_preference.NotificationPreference(
                        email = True, ), 
                    buy_now_transmission_rights_offers = empire_platform_api_public_client.models.notification_preference.NotificationPreference(
                        email = True, ), ),
                appearance = 'DEFAULT',
        )
        """

    def testUserPreferences(self):
        """Test UserPreferences"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

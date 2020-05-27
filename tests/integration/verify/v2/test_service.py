# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ServiceTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services.create(friendly_name="friendly_name")

        values = {'FriendlyName': "friendly_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services',
            data=values,
        ))

    def test_create_record_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "name",
                "code_length": 4,
                "lookup_enabled": false,
                "psd2_enabled": false,
                "skip_sms_to_landlines": false,
                "dtmf_input_required": false,
                "tts_name": "name",
                "mailer_sid": "MDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "do_not_share_warning_enabled": false,
                "custom_code_enabled": true,
                "push": {
                    "include_date": true,
                    "notify_service_sid": null
                },
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",
                    "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",
                    "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",
                    "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",
                    "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services.create(friendly_name="friendly_name")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_record_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "name",
                "code_length": 4,
                "lookup_enabled": false,
                "psd2_enabled": false,
                "skip_sms_to_landlines": false,
                "dtmf_input_required": false,
                "tts_name": "name",
                "mailer_sid": "MDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "do_not_share_warning_enabled": false,
                "custom_code_enabled": true,
                "push": {
                    "include_date": true,
                    "notify_service_sid": null
                },
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",
                    "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",
                    "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",
                    "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",
                    "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services',
        ))

    def test_read_all_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://verify.twilio.com/v2/Services?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "next_page_url": null,
                    "key": "services",
                    "url": "https://verify.twilio.com/v2/Services?PageSize=50&Page=0"
                },
                "services": [
                    {
                        "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "name",
                        "code_length": 4,
                        "lookup_enabled": false,
                        "psd2_enabled": false,
                        "skip_sms_to_landlines": false,
                        "dtmf_input_required": false,
                        "tts_name": "name",
                        "mailer_sid": "MDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "do_not_share_warning_enabled": false,
                        "custom_code_enabled": true,
                        "push": {
                            "include_date": true,
                            "notify_service_sid": null
                        },
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",
                            "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",
                            "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",
                            "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",
                            "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.verify.v2.services.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_record_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "name",
                "code_length": 4,
                "lookup_enabled": false,
                "psd2_enabled": false,
                "skip_sms_to_landlines": false,
                "dtmf_input_required": false,
                "tts_name": "name",
                "mailer_sid": "MDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "do_not_share_warning_enabled": false,
                "custom_code_enabled": true,
                "push": {
                    "include_date": true,
                    "notify_service_sid": null
                },
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",
                    "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",
                    "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",
                    "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",
                    "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

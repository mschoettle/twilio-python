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


class GoodDataTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.good_data().create(token="token")

        headers = {'Token': "token", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Accounts/GoodData',
            headers=headers,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "session_expiry": "2022-09-27T09:28:01Z",
                "workspace_id": "clbi1eelh1x8z4.......ijpnyu",
                "session_id": "-----BEGIN PGP MESSAGE-----\\n\\nwcBMA11tX1FL13rp\\u2026\\u2026kHXd\\n=vOBk\\n-----END PGP MESSAGE-----\\n",
                "gd_base_url": "https://analytics.ytica.com/",
                "url": "https://flex-api.twilio.com/v1/Accounts/GoodData"
            }
            '''
        ))

        actual = self.client.flex_api.v1.good_data().create()

        self.assertIsNotNone(actual)

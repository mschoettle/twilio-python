# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class WorkflowTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .workflows(sid="WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .workflows(sid="WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .workflows(sid="WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_read_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .workflows.read()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows',
        ))

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .workflows.create(friendly_name="friendly_name", configuration="configuration", assignment_callback_url="/example")
        
        values = {
            'FriendlyName': "friendly_name",
            'Configuration': "configuration",
            'AssignmentCallbackUrl': "/example",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows',
            data=values,
        ))
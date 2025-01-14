"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
import datetime

import freeclimb
from freeclimb.model.capabilities import Capabilities
globals()['Capabilities'] = Capabilities

from freeclimb.model.incoming_number_result_all_of import IncomingNumberResultAllOf  # noqa: E501


class TestIncomingNumberResultAllOf(unittest.TestCase):
    """IncomingNumberResultAllOf unit test stubs"""

    def setUp(self):
        self.model = IncomingNumberResultAllOf()

    def test_capabilities(self):
        """Test IncomingNumberResultAllOf.capabilities"""
        object = Capabilities(sms=False, voice=False,
                              toll_free=False, ten_dlc=False, short_code=False)
        self.model.capabilities = object
        assert self.model.get("capabilities", object)

    def test_campaign_id(self):
        """Test IncomingNumberResultAllOf.campaign_id"""
        self.model.campaign_id = "TEST_STRING"
        assert self.model.get("campaign_id") == "TEST_STRING"

    def test_phone_number_id(self):
        """Test IncomingNumberResultAllOf.phone_number_id"""
        self.model.phone_number_id = "TEST_STRING"
        assert self.model.get("phone_number_id") == "TEST_STRING"

    def test_account_id(self):
        """Test IncomingNumberResultAllOf.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.get("account_id") == "TEST_STRING"

    def test_application_id(self):
        """Test IncomingNumberResultAllOf.application_id"""
        self.model.application_id = "TEST_STRING"
        assert self.model.get("application_id") == "TEST_STRING"

    def test_phone_number(self):
        """Test IncomingNumberResultAllOf.phone_number"""
        self.model.phone_number = "TEST_STRING"
        assert self.model.get("phone_number") == "TEST_STRING"

    def test_alias(self):
        """Test IncomingNumberResultAllOf.alias"""
        self.model.alias = "TEST_STRING"
        assert self.model.get("alias") == "TEST_STRING"

    def test_region(self):
        """Test IncomingNumberResultAllOf.region"""
        self.model.region = "TEST_STRING"
        assert self.model.get("region") == "TEST_STRING"

    def test_country(self):
        """Test IncomingNumberResultAllOf.country"""
        self.model.country = "TEST_STRING"
        assert self.model.get("country") == "TEST_STRING"

    def test_voice_enabled(self):
        """Test IncomingNumberResultAllOf.voice_enabled"""
        self.model.voice_enabled = False
        assert self.model.get("voice_enabled") == False

    def test_sms_enabled(self):
        """Test IncomingNumberResultAllOf.sms_enabled"""
        self.model.sms_enabled = False
        assert self.model.get("sms_enabled") == False

    def test_offnet(self):
        """Test IncomingNumberResultAllOf.offnet"""
        self.model.offnet = False
        assert self.model.get("offnet") == False


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Golem unlimited low level hub API

    API description in Markdown.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import gu_rest_api
from gu_rest_api.api.peer_session_api import PeerSessionApi  # noqa: E501
from gu_rest_api.rest import ApiException


class TestPeerSessionApi(unittest.TestCase):
    """PeerSessionApi unit test stubs"""

    def setUp(self):
        self.api = gu_rest_api.api.peer_session_api.PeerSessionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_peer_session(self):
        """Test case for create_peer_session

        """
        pass

    def test_delete_peer_session(self):
        """Test case for delete_peer_session

        """
        pass

    def test_update_peer_session(self):
        """Test case for update_peer_session

        Sends multiple commands for peer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
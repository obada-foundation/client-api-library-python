"""
    OBADA API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: techops@obada.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import obada_client
from obada_client.api.obit_api import ObitApi  # noqa: E501


class TestObitApi(unittest.TestCase):
    """ObitApi unit test stubs"""

    def setUp(self):
        self.api = ObitApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get(self):
        """Test case for get

        Get Obit by DID or USN  # noqa: E501
        """
        pass

    def test_history(self):
        """Test case for history

        Get Obit history by DID or USN  # noqa: E501
        """
        pass

    def test_save(self):
        """Test case for save

        Save Obit  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        Search obits by query  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

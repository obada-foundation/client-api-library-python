"""
    OBADA API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: techops@obada.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import obada_client
from obada_client.model.account import Account
globals()['Account'] = Account
from obada_client.model.accounts import Accounts


class TestAccounts(unittest.TestCase):
    """Accounts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccounts(self):
        """Test Accounts"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Accounts()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
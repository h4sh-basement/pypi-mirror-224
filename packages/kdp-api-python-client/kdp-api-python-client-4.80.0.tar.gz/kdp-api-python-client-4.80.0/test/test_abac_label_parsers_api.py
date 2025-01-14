"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces. Please note that the Python client library follows Python's naming convention of snake casing for fields, even though they may appear in camel case in the API specification.  # noqa: E501

    The version of the OpenAPI document: 4.80.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import kdp_api
from kdp_api.api.abac_label_parsers_api import AbacLabelParsersApi  # noqa: E501


class TestAbacLabelParsersApi(unittest.TestCase):
    """AbacLabelParsersApi unit test stubs"""

    def setUp(self):
        self.api = AbacLabelParsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_abac_label_parsers(self):
        """Test case for get_abac_label_parsers

        Retrieves a list of Abac Label Parsers  # noqa: E501
        """
        pass

    def test_get_abac_label_parsers_id(self):
        """Test case for get_abac_label_parsers_id

        Retrieves Abac Label Parser with the given ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces. Please note that the Python client library follows Python's naming convention of snake casing for fields, even though they may appear in camel case in the API specification.  # noqa: E501

    The version of the OpenAPI document: 4.80.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import kdp_api
from kdp_api.api.attributes_api import AttributesApi  # noqa: E501


class TestAttributesApi(unittest.TestCase):
    """AttributesApi unit test stubs"""

    def setUp(self):
        self.api = AttributesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_attributes_id(self):
        """Test case for delete_attributes_id

        Remove Attribute with the given ID  # noqa: E501
        """
        pass

    def test_get_attributes(self):
        """Test case for get_attributes

        Retrieves a list of Attributes  # noqa: E501
        """
        pass

    def test_get_attributes_id(self):
        """Test case for get_attributes_id

        Retrieve Attribute with the given ID  # noqa: E501
        """
        pass

    def test_patch_attributes_id(self):
        """Test case for patch_attributes_id

        Update provided fields of Attribute with the given ID  # noqa: E501
        """
        pass

    def test_post_attributes(self):
        """Test case for post_attributes

        Creates a new Attribute  # noqa: E501
        """
        pass

    def test_put_attributes_id(self):
        """Test case for put_attributes_id

        Update Attribute with the given ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

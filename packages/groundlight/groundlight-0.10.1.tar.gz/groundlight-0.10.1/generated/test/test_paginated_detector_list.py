"""
    Groundlight API

    Ask visual queries.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: support@groundlight.ai
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.detector import Detector

globals()["Detector"] = Detector
from openapi_client.model.paginated_detector_list import PaginatedDetectorList


class TestPaginatedDetectorList(unittest.TestCase):
    """PaginatedDetectorList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedDetectorList(self):
        """Test PaginatedDetectorList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedDetectorList()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

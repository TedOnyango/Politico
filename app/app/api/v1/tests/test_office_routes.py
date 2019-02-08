from app import app
import unittest
import json

from app.api.v1.models.officemodels import OFFICES



class RoutesBaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app("testing")
        self.client = self.app.test_client()
        self.office1 = {
            "type": "Governor",
            "name": "Governor Webuye"
        }
        self.erroroffice = {
        }
    # tear down tests

    def tearDown(self):
        """Tperform final cleanup after tests run"""
        self.app.testing = False



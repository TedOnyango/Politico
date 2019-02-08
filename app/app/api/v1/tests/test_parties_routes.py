
from app import app
import unittest
import json

from app.api.v1.models.partymodels import PARTIES

class RoutesBaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app("testing")
        self.client = self.app.test_client()
        self.party1 = {
            "name": "Party 1",
            "logoUrl": ""
        }
        self.partytodelete = {
            "name": "Party 10",
            "logoUrl": ""
        }
        self.invalidparty = {
            "_id": 1
        }

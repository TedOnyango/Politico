
from app import createapp
import unittest
import json

from app.api.v1.models.partymodels import PARTIES

class RoutesBaseTest(unittest.TestCase):
    def setUp(self):
        self.app = createapp()
        self.client = self.app.test_client()
        self.party1 = {
            "name": "Part Theo",
            "logoUrl": ""
        }
        self.partytodelete = {
            "name": "Party 230",
            "logoUrl": ""
        }
        self.invalidparty = {
            "_id": 1
        }

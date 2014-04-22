from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
from index.views import *


class SimpleTest(unittest.TestCase):
    
    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


class SaveIpMethodTests(TestCase):

    def testIsIpSaved(self):
        self.assertEqual(saveIp('123.0.0.2'), True)

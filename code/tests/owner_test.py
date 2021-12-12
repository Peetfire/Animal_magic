import unittest
from unittest import result

from models.animal import Animal
from models.owner import Owner

class TestOwner(unittest.TestCase):

    def setUp(self):
        self.owner1 = Owner("Chatty Bob", "bobchat@gamil.com", "07982 543 627")
        self.animal1 = Animal("Mushroom MacGee", "Cat", "10/12/2017", self.owner1)

    def test_has_name(self):
        expected = "Chatty Bob"
        result = self.owner1.get_name()
        self.assertEqual(expected, result)

    def test_has_email(self):
        expected = "bobchat@gamil.com"
        result = self.owner1.get_email()
        self.assertEqual(expected, result)
        
    def test_has_phone(self):
        expected = "07982 543 627"
        result = self.owner1.get_phone()
        self.assertEqual(expected, result)

    def test_has_id(self):
        expected = None
        result = self.owner1.get_id()
        self.assertEqual(expected, result)

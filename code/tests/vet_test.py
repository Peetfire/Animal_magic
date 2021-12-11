import unittest
from unittest import result

from models.Vet import Vet
from models.Animal import Animal
from models.Owner import Owner

class TestVet(unittest.TestCase):

    def setUp(self):
        self.owner1 = Owner("Chatty Bob", "bobchat@gamil.com", "07982 543 627")
        self.animal1 = Animal("Mushroom MacGee", "Cat", "10/12/2017", self.owner1)
        self.vet1 = Vet("Supervet", self.animal1)

    def test_has_name(self):
        expected = "Supervet"
        result = self.vet1.get_name()
        self.assertEqual(expected, result)

    def test_has_animal(self):
        expected = self.animal1
        result = self.vet1.get_animal()
        self.assertEqual(expected, result)

    def test_has_id(self):
        expected = None
        result = self.vet1.get_id()
        self.assertEqual(expected, result)

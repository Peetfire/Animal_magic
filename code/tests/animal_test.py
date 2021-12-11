import unittest
from unittest import result

from models.Appointments import Appointment
from models.Vet import Vet
from models.Animal import Animal
from models.Owner import Owner

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.owner1 = Owner("Chatty Bob", "bobchat@gamil.com", "07982 543 627")
        self.animal1 = Animal("Mushroom MacGee", "Cat", "10/12/2017", self.owner1)
        self.vet1 = Vet("Supervet", self.animal1)
        self.appt1 = Appointment("This is a note", "12/12/2021", self.vet1, self.animal1)

    def test_has_name(self):
        expected = "Mushroom MacGee"
        result = self.animal1.get_name()
        self.assertEqual(expected, result)
        
    def test_has_species(self):
        expected = "Cat"
        result = self.animal1.get_species()
        self.assertEqual(expected, result)

    def test_has_dob(self):
        expected = "10/12/2017"
        result = self.animal1.get_dob()
        self.assertEqual(expected, result)
        
    def test_has_vet(self):
        expected = self.owner1
        result = self.animal1.get_owner()
        self.assertEqual(expected, result)

    def test_has_id(self):
        expected = None
        result = self.animal1.get_id()
        self.assertEqual(expected, result)
import unittest
from unittest import result

from models.Appointments import Appointment
from models.Vet import Vet
from models.Animal import Animal
from models.Owner import Owner

class TestAppointment(unittest.TestCase):

    def setUp(self):
        self.owner1 = Owner("Chatty Bob", "bobchat@gamil.com", "07982 543 627")
        self.animal1 = Animal("Mushroom MacGee", "Cat", "10/12/2017", self.owner1)
        self.vet1 = Vet("Supervet", self.animal1)
        self.appt1 = Appointment("This is a note", "12/12/2021", self.vet1, self.animal1)

    def test_has_note(self):
        expected = "This is a note"
        result = self.appt1.get_note_text()
        self.assertEqual(expected, result)
        
    def test_has_date(self):
        expected = "12/12/2021"
        result = self.appt1.get_appt_date()
        self.assertEqual(expected, result)

    def test_has_animal(self):
        expected = self.animal1
        result = self.appt1.get_animal()
        self.assertEqual(expected, result)
        
    def test_has_vet(self):
        expected = self.vet1
        result = self.appt1.get_vet()
        self.assertEqual(expected, result)

    def test_has_id(self):
        expected = None
        result = self.appt1.get_id()
        self.assertEqual(expected, result)
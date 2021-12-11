import unittest

from models.Vet import Vet
from models.Animal import Animal
from models.Owner import Onwer

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.owner1 = Owner()
        self.animal1 = Animal("Mushroom MacGee", "Cat", "10/12/2017", self.owner1)
        self.vet1 = Vet("Supervet", self.animal1)
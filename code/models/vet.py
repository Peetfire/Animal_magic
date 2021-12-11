class Vet:
	def __init__(self, name, animal, id = None):
		self.name = name
		self.animal = animal
		self.id = id 
		
	def get_name(self):
		return self.name

	def get_animal(self):
		return self.animal

	def get_id(self):
		return self.id

	def __str__():
 		return "name: " + name + " , " + "animal: " + animal + " , " + "id = None: " + id = None

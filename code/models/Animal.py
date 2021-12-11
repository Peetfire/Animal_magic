class Animal:
	def __init__(self, name, species, dob, owner, id=None):
		self.name = name
		self.species = species
		self.dob = dob
		self.owner = owner
		self.id = id

	def get_name(self):
		return self.name

	def get_species(self):
		return self.species

	def get_dob(self):
		return self.dob

	def get_owner(self):
		return self.owner

	def get_id(self):
		return self.id


	def __str__():
 		return "undefined: " + undefined + " , " + "name: " + name + " , " + "species: " + species + " , " + "dob: " + dob + " , " + "owner: " + owner + " , " + "id: " + id

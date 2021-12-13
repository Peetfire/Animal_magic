class Animal:
	def __init__(self, name, species, dob, owner, vet, id=None):
		self.name = name
		self.species = species
		self.dob = dob
		self.owner = owner
		self.vet = vet
		self.id = id

	def get_name(self):
		return self.name

	def get_species(self):
		return self.species

	def get_dob(self):
		return self.dob

	def get_owner(self):
		return self.owner.name

	def get_vet(self):
		return self.vet.name

	def get_id(self):
		return self.id

	def get_headings(self):
		return ["Name", "Species", "DoB", "Owner", "Vet"]

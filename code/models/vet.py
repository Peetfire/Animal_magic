class Vet:
	def __init__(self, name,  id = None):
		self.name = name
		self.id = id 
		
	def get_name(self):
		return self.name

	def get_id(self):
		return self.id

	def get_headings(self):
		return ["Name"]


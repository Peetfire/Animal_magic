class Owner:
	def __init__(self, name, email, phone, id=None):
		self.name = name
		self.email = email
		self.phone = phone
		self.id = id
		
	def get_name(self):
		return self.name

	def get_email(self):
		return self.email

	def get_phone(self):
		return self.phone

	def get_id(self):
		return self.id


	def __str__():
 		return "name: " + name + " , " + "email: " + email + " , " + "phone: " + phone + " , " + "id: " + id

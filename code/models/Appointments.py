class Appointments:
	def __init__(self, note_text, appt_date, vet, pet, id=None):
		self.note_text = note_text
		self.appt_date = appt_date
		self.vet = vet
		self.pet = pet
		self.id = id
		
	def get_note_text(self):
		return self.note_text

	def get_appt_date(self):
		return self.appt_date

	def get_vet(self):
		return self.vet

	def get_pet(self):
		return self.pet

	def get_id(self):
		return self.id


	def __str__():
 		return f"note_text: {note_text}, appt_date: {appt_date}, vet: {vet}, pet: {pet}, id: {id}"

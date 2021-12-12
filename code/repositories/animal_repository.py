# import db
from db.run_sql import run_sql

# # import models
# from models.appointment import Appointment
# from models.animal import Animal
# from models.owner import Owner  
# from models.vet import Vet
# # import repositories
# import appointment_repository as appt_repo
# import vet_repository as vet_repo
# import animal_repository as animal_repo

# Save
def save(animal):
    sql = "INSERT INTO animals (name, species, dob, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [animal.name, animal.species, animal.dob, animal.owner.id, animal.vet.id]
    results = run_sql(sql, values)
    animal.id = results[0]['id']

# Select All

# Select id

# Delete All
def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

# Delete id

# Update 
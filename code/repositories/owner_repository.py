from db.run_sql import run_sql

# import models
# from models.appointment import Appointment
# from models.animal import Animal
# from models.owner import Owner  
# from models.vet import Vet
# # import repositories
# import appointment_repository as appt_repo
# import vet_repository as vet_repo
# import animal_repository as animal_repo

# Save
def save(owner):
    sql = "INSERT INTO owners (name, email, phone) VALUES (%s, %s, %s) RETURNING id"
    values = [owner.name, owner.email, owner.phone]
    results = run_sql(sql, values)
    owner.id = results[0]['id']

# Select All

# Select id

# Delete All
def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)
# Delete id

# Update 
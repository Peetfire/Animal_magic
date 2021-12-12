from db.run_sql import run_sql
from models.owner import Owner

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
def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for result in results:
        owner = Owner(result['name'], result['email'], result['phone'], result['id'])
        owners.append(owner)
    return owners

# Select id
def select(id):
    sql = "SELECT * FROM appointments WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    owner = Owner(result['name'], result['email'], result['phone'], result['id'])
    return owner

# Delete All
def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)
# Delete id

# Update 
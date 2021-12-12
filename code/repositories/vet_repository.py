from db.run_sql import run_sql

# import models
# from models.appointment import Appointment
# from models.animal import Animal
# from models.owner import Owner  
from models.vet import Vet
# # import repositories
# # import appointment_repository as appt_repo
# import vet_repository as vet_repo
# import animal_repository as animal_repo

# Save
def save (vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING id"
    values = [vet.name]
    results = run_sql(sql, values)
    vet.id = results[0]['id']

# Select All
def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for result in results:
        vet = Vet(result['name'], result['id'])
        vets.append(vet)
    return vets

# Select id
def select(id):
    sql = "SELECT * FROM vets WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    vet = Vet(result['name'], result['id'])
    return vet

# Delete All
def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)
# Delete id

# Update 
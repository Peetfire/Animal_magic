# import db
from db.run_sql import run_sql
import pdb
# import models
from models.appointment import Appointment
# from models.animal import Animal
# from models.owner import Owner  
# from models.vet import Vet

# # import repositories
# import appointment_repository as appt_repo
import repositories.vet_repository as vet_repo
import repositories.animal_repository as animal_repo
# import owner_repository as owner_repo

# Save
def save(appt):
    sql = "INSERT INTO appointments (note_text, appt_date, animal_id, vet_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [appt.note_text, appt.appt_date, appt.animal.id, appt.vet.id]
    results = run_sql(sql, values)
    appt.id = results[0]['id']
    
def select_all():
    appts = []
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for result in results:
        vet = vet_repo.select(result['vet_id'])
        
        animal = animal_repo.select(result['animal_id'])
        appt = Appointment(result['note_text'], result['appt_date'], vet, animal, result['id'])
        appts.append(appt)
    return appts

# Select id
def select(id):
    sql = "SELECT * FROM appointments WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    vet = vet_repo.select(result['vet_id'])
    animal = animal_repo.select(result['animal_id'])
    appt = Appointment(result['note_text'], result['appt_date'], vet, animal, result['id'])
    return appt

# Delete All
def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)

# Delete id
def delete(id):
    sql = "DELETE FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)
# Update 
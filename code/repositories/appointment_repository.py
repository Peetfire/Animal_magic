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
    sql = "INSERT INTO appointments (note_text, appt_date, animal_id, vet_id) VALUES (%s, TO_DATE(%s, 'DD/MM/YYYY'), %s, %s) RETURNING id"
    values = [appt.note_text, appt.appt_date, appt.animal.id, appt.vet.id]
    results = run_sql(sql, values)
    appt.id = results[0]['id']
    
def select_all():
    appts = []
    sql = "SELECT * FROM appointments ORDER BY appt_date DESC"
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
def update(appt):
    sql = "UPDATE appointments SET (note_text, appt_date, animal_id, vet_id) = \
        (%s, TO_DATE(%s, 'DD/MM/YYYY'), %s, %s) WHERE id = %s"
    values = [appt.get_note_text(), appt.get_appt_date(), \
        appt.animal.get_id(), appt.vet.get_id(), appt.get_id()]
    run_sql(sql, values)

# SELECT ALL for VET
def select_vet_appts(vet):
    appts = []
    sql = "SELECT * FROM appointments WHERE vet_id = %s ORDER BY appt_date DESC"
    values = [vet.id]
    results = run_sql(sql, values)
    for result in results:
        vet = vet_repo.select(result['vet_id'])
        animal = animal_repo.select(result['animal_id'])
        appt = Appointment(result['note_text'], result['appt_date'], vet, animal, result['id'])
        appts.append(appt)
    return appts

# SELECT ALL for Owner
def select_owner_appts(owner):
    appts = []
    sql = "SELECT appointments.* FROM appointments INNER JOIN animals ON animals.id = appointments.animal_id WHERE animals.owner_id = %s ORDER BY appt_date DESC"
    values = [owner.id]
    results = run_sql(sql, values)
    for result in results:
        vet = vet_repo.select(result['vet_id'])
        animal = animal_repo.select(result['animal_id'])
        appt = Appointment(result['note_text'], result['appt_date'], vet, animal, result['id'])
        appts.append(appt)
    return appts

# SELECT ALL for Animal
def select_animal_appts(animal):
    appts = []
    sql = "SELECT appointments.* FROM appointments WHERE animal_id =  %s"
    values = [animal.id]
    results = run_sql(sql, values)
    for result in results:
        vet = vet_repo.select(result['vet_id'])
        animal = animal_repo.select(result['animal_id'])
        appt = Appointment(result['note_text'], result['appt_date'], vet, animal, result['id'])
        appts.append(appt)
    return appts

# Select ALL appointments sorted by <selected>
def select_all_sorted_by(sort_type, order):
    appts = []
    sql = f"SELECT appointments.* FROM appointments ORDER BY {sort_type} {order}"
    results = run_sql(sql)
    for result in results:
        vet = vet_repo.select(result['vet_id'])
        animal = animal_repo.select(result['animal_id'])
        appt = Appointment(result['note_text'], result['appt_date'], vet, animal, result['id'])
        appts.append(appt)
    return appts

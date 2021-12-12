# import db
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
def save(appt):
    sql = "INSERT INTO appointments (note_text, appt_date, animal_id, vet_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [appt.note_text, appt.appt_date, appt.animal.id, appt.vet.id]
    results = run_sql(sql, values)
    appt.id = results[0]['id']
    
# Select All
# def select_all():
#     appts = []
#     sql = "SELECT * FROM appointments"
#     results = run_sql(sql)

#     for result in results:
#         appt = Appointment(result['note_text'], result['appt_date'], vet)

# Select id

# Delete All

# Delete id

# Update 
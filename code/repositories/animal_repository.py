# import db
from db.run_sql import run_sql
import pdb

# # import models
# from models.appointment import Appointment
from models.animal import Animal
# from models.owner import Owner  
# from models.vet import Vet

# # import repositories
# import appointment_repository as appt_repo
import repositories.vet_repository as vet_repo
import repositories.owner_repository as owner_repo
# import animal_repository as animal_repo

# Save
def save(animal):
    sql = "INSERT INTO animals (name, species, dob, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [animal.name, animal.species, animal.dob, animal.owner.id, animal.vet.id]
    results = run_sql(sql, values)
    animal.id = results[0]['id']

# Select All
def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for result in results:
        vet = vet_repo.select(result['vet_id'])
        
        owner = owner_repo.select(result['owner_id'])
        animal = Animal(result['name'], result['species'], result['dob'], owner, vet, result['id'])
        animals.append(animal)
    return animals

# Select id
def select(id):
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    vet = vet_repo.select(result['vet_id'])
    owner = owner_repo.select(result['owner_id'])
    animal = Animal(result['name'], result['species'], result['dob'], owner, vet, result['id'])
    return animal

# Delete All
def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

# Delete id

# Update 
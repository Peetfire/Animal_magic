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
def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Update 
def update(animal):
    sql = "UPDATE animals SET (name, species, dob, owner_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.get_name(), animal.get_species(), animal.get_dob(), animal.owner.get_id(), animal.vet.get_id(), animal.get_id()]
    run_sql(sql, values)

# SELECT all animals of vet
def select_vet_animals(vet):
    animals = []
    sql = "SELECT * FROM animals WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql, values)
    for result in results:
        vet = vet_repo.select(result['vet_id'])
        owner = owner_repo.select(result['owner_id'])
        animal = Animal(result['name'], result['species'], result['dob'], owner, vet, result['id'])
        animals.append(animal)
    return animals

# SELECT ALL for Owner
def select_owner_animals(owner):
    animals = []
    sql = "SELECT * FROM animals WHERE owner_id = %s"
    values = [owner.id]
    results = run_sql(sql, values)
    for result in results:
        vet = vet_repo.select(result['vet_id'])
        owner = owner_repo.select(result['owner_id'])
        animal = Animal(result['name'], result['species'], result['dob'], owner, vet, result['id'])
        animals.append(animal)
    return animals
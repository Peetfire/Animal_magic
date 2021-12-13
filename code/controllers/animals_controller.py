from os import name, supports_effective_ids
from flask import Blueprint, Flask, blueprints, redirect, render_template, request
from models.animal import Animal

# import models and repos
# from models.vet import Vet
import repositories.vet_repository as vet_repo
import repositories.animal_repository as animal_repo
# import repositories.appointment_repository as appt_repo
import repositories.owner_repository as owner_repo


# set up blueprint
animals_blueprint = Blueprint("animals", __name__)

# INDEX
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repo.select_all()
    return render_template("animals/index.html", all_animals=animals)

# VIEW
@animals_blueprint.route("/animals/<id>")
def view_animal(id):
    animal = animal_repo.select(id)
    return render_template("animals/view.html", animal=animal)

# NEW
@animals_blueprint.route("/animals/add")
def new_animal():
    vets = vet_repo.select_all()
    owners = owner_repo.select_all()
    return render_template("/animals/add.html", vets=vets, owners=owners)

# CREATE
@animals_blueprint.route("/animals", methods=['POST'])
def create_animal():
    name = request.form['name']
    species = request.form['species']
    dob = request.form['dob']
    owner_id = request.form['owner_id']
    vet_id = request.form['vet_id']
    owner = owner_repo.select(owner_id)
    vet = vet_repo.select(vet_id)
    animal = Animal(name, species, dob, owner, vet)
    animal_repo.save(animal)
    return redirect("/animals")

# EDIT



# UPDATE




# DELETE
@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repo.delete(id)
    return redirect("/animals")
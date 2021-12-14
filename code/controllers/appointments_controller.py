from flask import Blueprint, Flask, redirect, render_template, request
from models.appointment import Appointment

# import models and repos
# from models.vet import Vet
import repositories.vet_repository as vet_repo
import repositories.animal_repository as animal_repo
import repositories.appointment_repository as appt_repo
# import repositories.owner_repository as owner_repo


# set up blueprint
appointments_blueprint = Blueprint("appointments", __name__)

# INDEX
@appointments_blueprint.route("/appts")
def appointments():
    appts = appt_repo.select_all()  
    return render_template("appts/index.html", all_appts=appts)

# VIEW
@appointments_blueprint.route("/appts/<id>")
def view_appt(id):
    appt = appt_repo.select(id)
    return render_template("appts/view.html", appt=appt)

# NEW
@appointments_blueprint.route("/appts/add")
def new_appt():
    animals = animal_repo.select_all()
    vets = vet_repo.select_all()
    return render_template("/appts/add.html", animals=animals, vets=vets)

# CREATE
@appointments_blueprint.route("/appts", methods=['POST'])
def create_appt():
    appt_date = request.form['date']
    animal_id = request.form['animal_id']
    vet_id = request.form['vet_id']
    note_text = request.form['note_text']
    vet = vet_repo.select(vet_id)
    animal = animal_repo.select(animal_id)
    appt = Appointment(note_text, appt_date, vet, animal)
    appt_repo.save(appt)
    return redirect("/appts")


# EDIT
@appointments_blueprint.route("/appts/<id>/edit")
def edit_appt(id):
    appt = appt_repo.select(id)
    animals = animal_repo.select_all()
    vets = vet_repo.select_all()
    return render_template("/appts/edit.html", appt=appt, animals=animals, vets=vets)

# UPDATE
@appointments_blueprint.route("/appts/<id>", methods=['POST'])
def update_appt(id):
    appt_date = request.form['date']
    animal_id = request.form['animal_id']
    vet_id = request.form['vet_id']
    note_text = request.form['note_text']
    vet = vet_repo.select(vet_id)
    animal = animal_repo.select(animal_id)
    appt = Appointment(note_text, appt_date, vet, animal, id)
    appt_repo.update(appt)
    return redirect("/appts")


# DELETE
@appointments_blueprint.route("/appts/<id>/delete", methods=['POST'])
def delete_appt(id):
    appt_repo.delete(id)
    return redirect("/appts")
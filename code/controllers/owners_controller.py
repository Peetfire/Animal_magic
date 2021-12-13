from flask import Blueprint, Flask, redirect, render_template, request

# import models and repos
# from models.vet import Vet
# import repositories.vet_repository as vet_repo
# import repositories.animal_repository as animal_repo
# import repositories.appointment_repository as appt_repo
import repositories.owner_repository as owner_repo


# set up blueprint
owners_blueprint = Blueprint("owners", __name__)

# INDEX
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repo.select_all()
    return render_template("owners/index.html", all_owners = owners)

# VIEW
@owners_blueprint.route("/owners/<id>")
def view_owner(id):
    owner = owner_repo.select(id)
    return render_template("owners/view.html", owner=owner)
# NEW



# CREATE



# EDIT



# UPDATE




# DELETE

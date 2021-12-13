from flask import Blueprint, Flask, redirect, render_template, request

# import models and repos
# from models.vet import Vet
import repositories.vet_repository as vet_repo
# import repositories.animal_repository as animal_repo
# import repositories.appointment_repository as appt_repo
# import repositories.owner_repository as owner_repo


# set up blueprint
vets_blueprint = Blueprint("vets", __name__)

# INDEX
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repo.select_all()
    return render_template("vets/index.html", all_vets = vets)

# VIEW
@vets_blueprint.route("/vets/<id>")
def view_vet(id):
    vet = vet_repo.select(id)
    return render_template("/vets/view.html", vet=vet)
# NEW



# CREATE



# EDIT



# UPDATE




# DELETE

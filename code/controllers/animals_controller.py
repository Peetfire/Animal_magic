from flask import Blueprint, Flask, blueprints, redirect, render_template, request

# import models and repos
# from models.vet import Vet
# import repositories.vet_repository as vet_repo
import repositories.animal_repository as animal_repo
# import repositories.appointment_repository as appt_repo
# import repositories.owner_repository as owner_repo


# set up blueprint
animals_blueprint = Blueprint("animals", __name__)

# INDEX
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repo.select_all()
    return render_template("animals/index.html", all_animals=animals)

# NEW



# CREATE



# EDIT



# UPDATE




# DELETE

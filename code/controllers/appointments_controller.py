from flask import Blueprint, Flask, redirect, render_template, request

# import models and repos
# from models.vet import Vet
# import repositories.vet_repository as vet_repo
# import repositories.animal_repository as animal_repo
import repositories.appointment_repository as appt_repo
# import repositories.owner_repository as owner_repo


# set up blueprint
appointments_blueprint = Blueprint("appointments", __name__)

# INDEX
@appointments_blueprint.route("/appts")
def appointments():
    appts = appt_repo.select_all()  
    return render_template("appts/index.html", all_appts=appts)

# NEW



# CREATE



# EDIT



# UPDATE




# DELETE

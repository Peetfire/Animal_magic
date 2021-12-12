# import models
# from models.appointment import Appointment
from models.animal import Animal
from models.appointment import Appointment
from models.owner import Owner  
from models.vet import Vet

# import repositories

import repositories.vet_repository as vet_repo
import repositories.owner_repository as owner_repo
import repositories.animal_repository as animal_repo
import repositories.appointment_repository as appt_repo

vet_repo.delete_all()
owner_repo.delete_all()
animal_repo.delete_all()
appt_repo.delete_all()

vet1 = Vet("Noel Fitzpatrick")
vet_repo.save(vet1)

owner1 = Owner("Bob Fordyce", "bob@gmail.com", "07986 456 123")
owner_repo.save(owner1)

animal1 = Animal("Slinky Malinky", "Cat", "07/04/2008", owner1, vet1)
animal_repo.save(animal1)

appt1 = Appointment("This is a note", "25/12/2021", vet1, animal1)
appt_repo.save(appt1)
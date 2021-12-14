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
vet2 = Vet("James Heriot")
vet_repo.save(vet2)
vet3 = Vet("Claude Bourgelat")
vet_repo.save(vet3)
vet4 = Vet("Mary Knight Dunlap")
vet_repo.save(vet4)

owner1 = Owner("Bob Fordyce", "bob@gmail.com", "07986 456 123")
owner_repo.save(owner1)
owner2 = Owner("Jane Keysdale", "jane@gmail.com", "07987 896 347")
owner_repo.save(owner2)
owner3 = Owner("Alison Halles", "Ally@gmail.com", "07988 889 127")
owner_repo.save(owner3)
owner4 = Owner("Barry Tymmil", "bazza@gmail.com", "07876 371 365")
owner_repo.save(owner4)

animal1 = Animal("Slinky Malinky", "Cat", "07/04/2008", owner1, vet1)
animal_repo.save(animal1)
animal2 = Animal("Hairy McClary", "Dog", "07/07/2017", owner1, vet1)
animal_repo.save(animal2)
animal3 = Animal("Grizzly McDuff", "Cat", "23/09/2008", owner2, vet2)
animal_repo.save(animal3)
animal4 = Animal("Bitzer Maloney", "Dog", "19/05/2012", owner3, vet3)
animal_repo.save(animal4)

# appt1 = Appointment("This is a note", "25/12/2021", animal1.vet, animal1)
# appt_repo.save(appt1)
# appt2 = Appointment("This is also a note", "01/01/2022", animal2.vet, animal2)
# appt_repo.save(appt2)
# appt3 = Appointment("This is a note", "02/01/2022", animal3.vet, animal3)
# appt_repo.save(appt3)
# appt4 = Appointment("This is a note", "03/01/2022", vet3, animal4)
# appt_repo.save(appt4)

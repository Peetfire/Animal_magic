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
animal5 = Animal("Butterball Brown", "Cat", "07/07/2014", owner4, vet3)
animal_repo.save(animal5)
animal6 = Animal("Muffin McClay", "Dog", "12/12/2015", owner4, vet4)
animal_repo.save(animal6)
animal7 = Animal("Graywake Jone", "Cat", "23/09/2022", owner2, vet4)
animal_repo.save(animal7)
animal8 = Animal("Schnitzel von Krumm", "Dog", "14/01/2016", owner3, vet3)
animal_repo.save(animal8)

appt1 = Appointment("Ate santa ornament", "25/12/2020", animal1.vet, animal1)
appt_repo.save(appt1)
appt2 = Appointment("Check-up post surgery: removal of santa", "01/01/2021", animal1.vet, animal1)
appt_repo.save(appt2)
appt3 = Appointment("Ate a bee: administered antihistamines", "02/03/2021", animal1.vet, animal1)
appt_repo.save(appt3)
appt4 = Appointment("Ate a bee: administered antihistamines", "02/03/2021", animal2.vet, animal2)
appt_repo.save(appt4)
appt5 = Appointment("Check up and booster shots.", "07/03/2021", animal3.vet, animal3)
appt_repo.save(appt5)
appt6 = Appointment("Stood on a bee: administered antihistamines", "23/05/2021", animal3.vet, animal3)
appt_repo.save(appt6)
appt7 = Appointment("Teeth cleaning - sedation required.", "17/08/2021", animal3.vet, animal3)
appt_repo.save(appt7)
appt8 = Appointment("Neutering and fist vacinations.", "03/05/2021", animal4.vet, animal4)
appt_repo.save(appt8)
appt9 = Appointment("Feel from tree: broken L rear leg. Set in cast & cone of shame.", "15/09/2021", animal4.vet, animal4)
appt_repo.save(appt9)
appt10 = Appointment("Cast removel and check-up: leg has healed well.", "22/10/2021", animal4.vet, animal4)
appt_repo.save(appt10)
appt11 = Appointment("Expolsive diarrhea: medication administered. charged extra for clean-up.", "02/01/2022", animal5.vet, animal5)
appt_repo.save(appt11)
appt12 = Appointment("Check-up and booster shots.", "03/01/2022", animal5.vet, animal5)
appt_repo.save(appt12)
appt13 = Appointment("Check-up and booster shots.", "03/01/2022", animal6.vet, animal6)
appt_repo.save(appt13)
appt12 = Appointment("Check-up and booster shots.", "03/01/2022", animal7.vet, animal7)
appt_repo.save(appt12)
appt12 = Appointment("Check-up and booster shots.", "03/01/2022", animal8.vet, animal8)
appt_repo.save(appt12)

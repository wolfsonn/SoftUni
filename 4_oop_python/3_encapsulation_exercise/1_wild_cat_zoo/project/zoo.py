from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.__workers_capzoozacity = int
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals) and price <= self.__budget:
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__}'
        elif self.__animal_capacity > 0 and price > self.__budget:
            return 'Not enough budget'
        else:
            return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name][0]
        if worker in self.workers:
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'
        else:
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        salaries = 0
        for w in self.workers:
            salaries += w.salary
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        else:
            return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        needs = 0
        for a in self.animals:
            needs += a.get_needs()
        if self.__budget >= needs:
            self.__budget -= needs
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        else:
            return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result = f'You have {len(self.animals)} animals'
        result += f'-----{len(lions)} Lions:\n'
        result += "\n".join(lions) + "\n"
        result += f'-----{len(tigers)} Lions:\n'
        result += "\n".join(tigers) + "\n"
        result += f'-----{len(cheetahs)} Lions:\n'
        result += "\n".join(cheetahs) + "\n"
        return result

    def workers_status(self):
        keepers = [a for a in self.workers if a.__class__.name == "Keeper"]
        caretakers = [a for a in self.workers if a.__class__.name == "Caretaker"]
        vets = [a for a in self.workers if a.__class__.name == "Vet"]
        result = f'You have {len(self.workers)} animals'
        result += f'-----{len(keepers)} Lions:\n'
        result += "\n".join(keepers) + "\n"
        result += f'-----{len(caretakers)} Lions:\n'
        result += "\n".join(caretakers) + "\n"
        result += f'-----{len(vets)} Lions:\n'
        result += "\n".join(vets) + "\n"
        return result



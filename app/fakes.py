from faker import Faker
from random import choice
from faker.providers import BaseProvider

import sys
sys.path.append('..')
from app.serial import Task

class TaskProvider(BaseProvider):
    def task_name(self):
        tasks = ['Acordar', 'Comer', 'Ir ao mercado', 'Malhar', 'Almoçar', 'Estudar', 'Jantar', 'Dormir']
        return choice(tasks)
    def state(self):
        states = ['ToDo', 'Doing', 'Done']
        return choice(states)

    def id(self):
        return self.random_int(0, 999)

    def task(self):
        return Task(self.task_name(), self.state(), self.id())

faker = Faker()
faker.add_provider(TaskProvider)
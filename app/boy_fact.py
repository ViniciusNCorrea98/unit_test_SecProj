from app.serial import Task
from factory import Factory, Faker

from app.fakes import TaskProvider

Faker.add_provider(TaskProvider)



#The Factory library will help us to create differents class based on a 'Task' class in serial.py
class TaskFactory(Factory):
    class Meta:
        model = Task

    task_name = Faker('task_name')
    state = Faker('state')
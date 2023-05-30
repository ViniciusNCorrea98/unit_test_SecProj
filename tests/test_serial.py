from unittest import TestCase, main
import sys

sys.path.append('..')
from app.serial import Task, task_serializer
class TestModelTask(TestCase):
    def test_model(self):
        esperado = 'Task(task_name="Acordar", state="ToDo")'
        chamada = Task('Acordar', 'ToDo')

        self.assertEqual(esperado, str(chamada))

    def check_type_id(self):
        chamada = Task('', '')
        self.assertIsInstance(chamada.id_, int)

class TestTaskSerializer(TestCase):
    def check_Task_is_dict(self):
        task_name = 'Ligar para o Gustavin'
        state = 'ToDo'

        task = Task(task_name, state)
        self.assertIsInstance(task_serializer(task), dict)

    def check_task_cannot_difference_dict(self):
        task_name = 'Ligar para o Gustavin'

        with self.assertRaises(AttributeError):
            task_serializer(task_name)



if __name__ == '__main__':
    main()
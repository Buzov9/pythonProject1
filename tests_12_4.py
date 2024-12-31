import unittest
import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            test_walk = Runner("test_obj_walk", speed=-5)
            for i in range(10):
                test_walk.walk()
            self.assertEqual(test_walk.distance, 50)
            logging.info(f'\'test-walk\' Выполнено успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            test_run = Runner(12.4)
            for i in range(10):
                test_run.run()
            self.assertEqual(test_run.distance, 100)
            logging.info(f'\'test-run\' Выполнено успешно')
        except:
            logging.error('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        test_obj1 = Runner('test_obj1')
        test_obj2 = Runner('test_obj2')
        for i in range(10):
            test_obj1.walk()
            test_obj2.run()
        self.assertNotEqual(test_obj1.distance, test_obj2.distance)



logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)
# t = Tournament(101, first, second)
# print(t.start())

import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        test_walk = Runner("test_obj_walk")
        for i in range(10):
            test_walk.walk()
        self.assertEqual(test_walk.distance, 50)

    def test_run(self):
        test_run = Runner("test_obj_run")
        for i in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    def test_challenge(self):
        test_obj1 = Runner('test_obj1')
        test_obj2 = Runner('test_obj2')
        for i in range(10):
            test_obj1.walk()
            test_obj2.run()
        self.assertNotEqual(test_obj1.distance, test_obj2.distance)


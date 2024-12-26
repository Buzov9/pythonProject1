import unittest
from tests_12_2 import Tournament, Runner


def freeze(func):
    def wrapper(self, *args, **kwargs):
        if not self.__class__.is_frozen:
            return func(self, *args, **kwargs)
        else:
            print(f'тесты заморожены')
        return wrapper
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze
    def test_walk(self):
        test_walk = Runner("test_obj_walk")
        for i in range(10):
            test_walk.walk()
        self.assertEqual(test_walk.distance, 500)

    @freeze
    def test_run(self):
        test_run = Runner("test_obj_run")
        for i in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    @freeze
    def test_challenge(self):
        test_obj1 = Runner('test_obj1')
        test_obj2 = Runner('test_obj2')
        for i in range(10):
            test_obj1.walk()
            test_obj2.run()
        self.assertNotEqual(test_obj1.distance, test_obj2.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.usain = Runner('Усэйн', 10)
        cls.andrey = Runner('Андрей', 9)
        cls.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, results in cls.all_results.items():
            print(f"Результаты теста {test_name}:")
            for place, runner in results.items():
                print(f"{place} место: {runner.name}")

    @freeze
    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results[self._testMethodName] = results
        self.assertTrue(results[max(results.keys())].name, self.usain.name)

    @freeze
    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[self._testMethodName] = results
        self.assertTrue(results[max(results.keys())].name, self.andrey.name)

    @freeze
    def test_all_runners(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[self._testMethodName] = results
        self.assertTrue(results[max(results.keys())].name, self.usain.name)


suite = unittest.TestSuite()
suite.addTest(RunnerTest('test'))
suite.addTest(TournamentTest('test'))
t = unittest.TextTestRunner(verbosity=2)


t.run(suite)


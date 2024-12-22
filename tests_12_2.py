import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(unittest.TestCase):
    all_results = {}

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

    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results[self._testMethodName] = results
        self.assertTrue(results[max(results.keys())].name, self.usain.name)

    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[self._testMethodName] = results
        self.assertTrue(results[max(results.keys())].name, self.andrey.name)

    def test_all_runners(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[self._testMethodName] = results
        self.assertTrue(results[max(results.keys())].name, self.usain.name)

if __name__ == '__main__':
    unittest.main()

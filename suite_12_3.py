import unittest
import tests_12_2

tests = unittest.TestSuite()
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.RunnerTest))
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)

runner.run(tests)



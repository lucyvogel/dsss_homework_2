import unittest
from math_quiz import random_integer, random_operation, evaluate_problem

class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        for _ in range(1000):
            rand_op = random_operation()
            self.assertIn(rand_op, ['+', '-', '*'])
        pass

    def test_evaluate_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 4, '*', '3 * 4', 12),
                (7, 1, '-', '7 - 1', 6)
            ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, result = evaluate_problem(num1, num2, operator)
                self.assertEqual(expected_answer, result)
                self.assertEqual(problem, expected_problem)

if __name__ == "__main__":
    unittest.main()

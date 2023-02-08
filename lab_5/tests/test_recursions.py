import unittest
import recursions as rec


class TestRecursions(unittest.TestCase):
    def test_recursion_max(self):
        test_cases = [
            ([1, 2, 3, 1, 2, 3], 3),
            ([], None),
            ([1, 1, 1], 1),
            ([10, 1, 2, 3], 10)
        ]
        for test in test_cases:
            test_case, right_answer = test
            mx = rec.recursion_max(test_case)
            self.assertEqual(mx, right_answer)

    def test_fibonacci(self):
        test_cases = [
            (-1, 0),
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 5),
            (5, 8),
            (9, 55)
        ]
        for test in test_cases:
            test_case, right_answer = test
            self.assertEqual(rec.fibonacci(test_case), right_answer)

    def test_pow_n(self):
        test_cases = [
            ([1, 1], 1),
            ([2, 0], 1),
            ([3, 2], 9),
            ([2], 256),
            ([3, 3], 27)
        ]
        for test in test_cases:
            test_case, right_answer = test
            self.assertEqual(rec.pow_n(*test_case), right_answer)

    def num_reverse(self):
        test_cases = [
            (123, 321),
            (111, 111),
            (4224, 4224),
            (4, 4),
            (123456789, 987654321)
        ]
        for test in test_cases:
            test_case, right_answer = test
            self.assertEqual(rec.num_reverse(test_case), right_answer)

from unittest import TestCase
import functions as func


class TestFunctions(TestCase):
    def test_add(self):
        test_case = [1, 2, 3], [4, 5, 6]
        right_answer = [5, 7, 9]
        self.assertEqual(func.add(*test_case), right_answer)

    def test_list_create(self):
        test_case = ['123', 123, None]
        self.assertEqual(func.list_create(*test_case), test_case)

    def test_is_bit_set(self):
        test_cases = [
            (1, 0, True),
            (1, 1, False),
            (0, 0, False),
            (7, 0, True),
            (7, 1, True),
            (7, 2, True),
            (7, 3, False)
        ]
        for test in test_cases:
            number, bit_id, right_answer = test
            self.assertEqual(func.is_bit_set(number, bit_id), right_answer)

    def test_gcd(self):
        test_cases = [
            (6, 3, 3),
            (6, 9, 3),
            (12, 16, 4),
            (11, 17, 1),
        ]
        for test in test_cases:
            a, b, right_answer = test
            self.assertEqual(func.gcd(a, b), right_answer)

    def test_volume_of_box(self):
        test_cases = [
            ([1], 70),
            ([1, 2], 20),
            ([1, 1, 1], 1),
        ]
        for test in test_cases:
            params, right_answer = test
            self.assertEqual(func.volume_of_box(*params), right_answer)

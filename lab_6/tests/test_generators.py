import unittest
import generators as gr


class TestGenerators(unittest.TestCase):
    def test_task_3(self):
        test_cases = [
            [1, 10, 3], 
            [5, 20, 2],
            [2, 2, 1]
        ]

        iterator = 1
        for test in test_cases:
            self.assertEqual(
                list(gr.my_generator(*test)),
                list(range(*test))
            )

    def test_enumerate(self):
        test_cases = [
            ['a', 'b', 'c', 'd', 'e'],
            [0, 1, 2, 3, 4],
            [0],
        ]

        for test in test_cases:
            generated_list = list(gr.my_enumerate(test))
            right_list = list(enumerate(test))
            self.assertEqual(generated_list, right_list)

    def test_my_pow(self):
        value = 2
        generator = gr.my_pow(value)
        for i in range(1, 10):
            self.assertEqual(value, next(generator))
            value *= value

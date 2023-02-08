import unittest
import list_comprehensions as lc


class TestListComprehensions(unittest.TestCase):

    def test_task_3(self):
        self.assertEqual(lc.task_3(5, 20), [15])

        right_array = [-30, -15, 0, 15, 30, 45]
        self.assertEqual(lc.task_3(-43, 57), right_array)

    def test_task_9(self):
        answer = lc.task_9([16, 15, 14])
        self.assertEqual(answer, [17, 15, 14])

        test_case = [1, 2, 3, 4, 9, 7, 4, 6, 22, 3, 84, 21, 45, 76]
        right_answer = [1, 2, 3, 4, 9, 7, 4, 6, 23, 3, 85, 22, 46, 77]
        self.assertEqual(lc.task_9(test_case), right_answer)

    def test_task_10(self):
        start, end = 0, 15
        right_answer = [1, 10, 11, 12, 13, 14]
        self.assertEqual(lc.task_10(start, end), right_answer)

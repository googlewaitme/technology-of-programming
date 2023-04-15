import unittest
import decorators as dc

import time
from datetime import timedelta

class TestDecorators(unittest.TestCase):
    def test_task_3(self):
        test_cases = [
            ("foo", "OOF"),
            ("udpate", "ETAPDU")
        ]
        for test in test_cases:
            param, right_answer = test
            self.assertEqual(dc.reverse_str(param), right_answer)

    def test_task_9(self):
        test_cases = [
            (1, 1),
            (2, 10),
            (10, 10)
        ]
        for test in test_cases:
            start_test = time.time()
            scored_time = dc.algebraic_sum(*test)
            real_time = time.time() - start_test
            different = real_time - scored_time
            self.assertLess(different, 1)
            


    def test_task_10(self):
        test_cases = [
            ((1, 2), 30),
            ((5, 6), 110),
            ((0, 0), 0),
            ((-4, -1), -50)
        ]
        for test in test_cases:
            params, right_answer = test
            self.assertEqual(dc.add(*params), right_answer)



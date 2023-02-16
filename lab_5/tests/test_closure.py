import unittest
import closures as cl


class TestClosures(unittest.TestCase):
    def test_task_3(self):
        '''
        closure_str return function
        '''
        test_string = '012345'
        test_cases = [
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (6, ''),
            (-1, ''),
        ]
        index_func = cl.closure_str(test_string)
        for test in test_cases:
            param, right_answer = test
            self.assertEqual(index_func(param), right_answer)
            

    def test_task_9(self):
        '''
        test closure_list_pow
        '''
        test_array = [4, 9, 16]
        test_cases = [
            (1, [4, 9, 16]),
            (0, [1, 1, 1]),
            (2, [16, 81, 256]),
            (0.5, [2, 3, 4])
        ]
        pow_func = cl.closure_list_pow(test_array)
        for test in test_cases:
            param, expected_value = test
            resulting_value = pow_func(param)
            self.assertEqual(resulting_value, expected_value)

    def test_task_10(self):
        test_array = list(range(10))
        test_cases = [
            (1, []),
            (2, [1, 3, 5, 7, 9]),
            (3, [1, 2, 4, 5, 7, 8]),
            (4, [1, 2, 3, 5, 6, 7, 9]),
            (11, list(range(1, 10))),
        ]
        del_func = cl.closure_list_del(test_array) 
        for test in test_cases:
            param, expected_value = test
            resulting_value = del_func(param)
            self.assertEqual(resulting_value, expected_value)

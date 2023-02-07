'''
created by bulat 07.02.2023
'''
from typing import List


def task_3(start: int, end: int) -> List[int]:
    '''
    Return an array where each element is divisible by both 3 and 5
    '''

    array = [el for el in range(start, end) if (el % 3 == 0  and el % 5 == 0)]
    return array

def task_9(array: List[int]) -> List[int]:
    """
    Increment each array element by one if it is greater than 15
    """

    new_array = [el+ 1 if el > 15 else el for el in array]
    return new_array

def task_10(start: int, end: int) -> List[int]:
    """
    return an array whose entry contains the number 1
    """

    array = [el for el in range(start, end) if '1' in str(el)]
    return array

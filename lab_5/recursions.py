from typing import List, Optional


def recursion_max(ls: List[int], index: int = 0, mx: Optional[int] = None) -> int:
    '''
    recursion method for search max in array
    '''
    if index == len(ls):
        return mx
    if mx is None:
        mx = ls[index]
    return recursion_max(ls, index+1, max(mx, ls[index]))

def fibonacci(count: int) -> int:
    '''
    recursion method for search fibocci number
    '''
    if count < 0:
        return 0
    if count <= 1:
        return 1
    return fibonacci(count-1) + fibonacci(count-2)

def pow_n(base: int, power: int = 8) -> int:
    '''
    raises number base to the power
    '''
    if power == 0:
        return 1
    if power == 1:
        return base
    if power % 2 == 0:
        return pow_n(base, power // 2) ** 2
    return pow_n(base, power-1) * base

def num_reverse(number: int, param: int = 0):
    '''
    reverse number: 1234 -> 4321
    '''
    if number == 0:
        return param
    last_cifr = number % 10
    return num_reverse(number // 10, param*10+last_cifr)

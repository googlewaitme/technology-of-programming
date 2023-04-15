'''
created by Bulat 16.02.2023
solving problems for decorators
'''
from typing import Callable
import time


def upcase_result(func: Callable[[str], str]) -> Callable[[str], str]:
    '''
    receives a function as input and returns the result of
    its operation in uppercase
    '''
    def wrapper(string: str):
        result = func(string)
        return result.upper()
    return wrapper

@upcase_result
def reverse_str(string: str) -> str:
    'return reverse string'
    return string[::-1]


def time_run(func: Callable[[int, float], float]) -> Callable[[int, float], float]:
    def wrapper(n: int, k: float):
        start = time.time()
        func(n, k)
        scored_time = time.time() - start
        return scored_time
    return wrapper

@time_run
def algebraic_sum(n: int, k: float):
    sm = 0
    for i in range(n+1):
        sm += i ** k
    return sm


def mul_result_factory(n: int):
    def mul_result(func: Callable[[float, float], float]) -> Callable[[float, float], float]:
        def wrapper(a: float, b:float):
            return func(a, b) * n
        return wrapper
    return mul_result

mul_result_10 = mul_result_factory(n=10)

@mul_result_10
def add(a: float, b: float):
    return a + b

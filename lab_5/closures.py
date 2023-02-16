from typing import List, Union, Callable


Digit = Union[int, float]

def closure_str(string: str) -> Callable[[int], str]:
    '''
    returns a funciton that returns the letter by index
    '''
    def str_index(index: int) -> str:
        if 0 <= index < len(string):
            return string[index]
        return ''
    return str_index

def closure_list_pow(array: List[Digit]) -> Callable[[Digit], List[Digit]]:
    def list_pow(pow_step: Digit) -> List[Digit]:
        return [el ** pow_step for el in array]
    return list_pow

def closure_list_del(array: List[int]) -> Callable[[int], List[int]]:
    def list_del(divisor: int) -> List[int]:
        return [el for el in array if el % divisor != 0]
    return list_del

'created by bulat 08.03.2023'
from typing import List, Union, Any


ArrayType = List[Union[int, float]]


def add(array1: ArrayType, array2: ArrayType) -> ArrayType:
    """
    take two arrays and returns an array with the sums of thier elements
    """
    new_array = []
    index = 0
    while index < len(array1) and index < len(array2):
        new_array.append(array1[index] + array2[index])
        index += 1
    while index < len(array1):
        new_array.append(array1[index])
        index += 1
    while index < len(array2):
        new_array.append(array2[index])
        index += 1
    return new_array

def list_create(a: Any, b: Any, c: Any) -> List[Any]:
    """
    take 3 random elements and return array with this elements
    """
    return [a, b, c]

def is_bit_set(number: int, bit_id: int) -> bool:
    """
    number: the integer whose bits are checking 
    bit_id: bit sequence number

    return: is the bit_id bit set to one
    """
    check_number = 1 << bit_id
    return number & check_number != 0

def gcd(a: int, b: int) -> int:
    """
    a, b: numbers whose common divisor is sought
    return greatest common divisor
    """
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def volume_of_box(l: int, h: int=7, w: int=10) -> int:
    """
    h: box height
    w: box width
    l: box length
    
    return: box volume
    """
    return l*h*w

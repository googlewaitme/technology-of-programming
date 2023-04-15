from typing import Any, Generator, Tuple, Union


def my_generator(start: int, end: int, step: int = 1) -> Generator[int, None, None]:
    iterator = start
    while iterator < end:
        yield iterator
        iterator += step


def my_enumerate(array: list[Any]) -> Generator[Tuple[Any, int], None, None]:
    index = 0
    for element in array:
        yield (index, element)
        index += 1


def my_pow(value: Union[int, float]) -> Generator[Union[int, float], None, None]:
    while 1:
        yield value
        value **= 1

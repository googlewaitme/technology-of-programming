from typing import List, Union


def task_3(ms: List[Union[int, float]]) -> Union[int, float]:
    print('\ntask-3')
    print(ms)
    index = 0
    sm = 0
    while index < len(ms):
        sm += ms[index]
        index += 1
    print('sum', sm)

def task_6(ms: List[Union[int, float]]):
    print('\ntask-6')
    print(ms)
    index = 0
    sm = 0
    while index < len(ms):
        if index % 2 == 1:
            sm += ms[index]
        index += 1
    print('sum', sm)

def task_7(ms: List[Union[int, float]]):
    print('\ntask-7')
    print(ms)
    index = 0
    count = 0
    while index < len(ms):
        if ms[index] == 2:
            count += 1
        index += 1
    print('count', count)

def task_17(start, end):
    print('\ntask-17')
    index = start 
    sm = 0
    while index % 4 != 0:
        index += 1
    while index <= end:
        index += 4
        sm += index
    print('sum', sm)
    return index

def task_14(z: int):
    print('\ntask-14')
    sm = 0
    for n in range(1, z):
        sm += (n - 20) / (n ** 1.5)    
    print("sum", sm)
    return sm


def main():
    task_3([1, 2, 3, 4, 9, 7, 4, 5.3, 9.7, 3])

    task_6([1, 2, 3, 4, 9, 7, 4, 5.3, 9.7, 3])

    task_7([1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2])

    task_17(start=-34, end=15)

    task_14(z=100)


if __name__ == "__main__":
    main()


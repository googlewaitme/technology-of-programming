from typing import List, Union

def task_5(val: int = 254):
    print('task-5')
    print(val)
    print('val // 4 = ', val // 4)

def task_6(val: int = 157):
    print('\ntask-6')
    print(val)
    print('val % 3 = ', val % 3)

def task_8(ms: List[Union[int, float]] = 157):
    print('\ntask-8')
    print(ms)
    print("ms[0] + ms[-1] =", ms[0] + ms[-1])

def task_12(n: int = 157):
    print('\ntask-12')
    print(n)
    print("value = ", (n-20)/(n**(3/2)))

def task_19(n: int = 157):
    print('\ntask-19')
    print(n)
    print("value = ", (2*n**2-4*n+10)/(2*n))

def main():
    task_5()
    task_6()
    task_8(ms=[1, 2, 3])
    task_12()
    task_19()

if __name__ == "__main__":
    main()


def task_4(a: int, b: int):
    print("\ntask_4")
    print("a, b =", a, b)
    if a % b == 0:
        print("Bingo!")
    else:
        print("a % b =", a % b)

def task_8():
    print("\ntask_8")
    n = int(input("Input n: "))
    if -15 <= n <= 10:
        print(f"yes, {n} in [-15, 10]")
    else:
        print(f"no, {n} not in [-15, 10]")

def task_10(a: int, b: int, c: int):
    b = -b
    c = 2 * c
    print('\ntask_10')
    print(f'{a}x^2 + {b}x + c = 0')
    if (a == 0) and (b == 0) and (c == 0):
        print('no answer')
        return None
    elif (a == 0):
        if (b == 0):
            print('no answer')
        else:
            print((-c) / b)
        return None
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        print('no answer')
    d = d ** 0.5
    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)
    if d == 0:
        print(x1)
    else:
        print(x1, x2)


def task_15(age: int):
    print('\ntask_15')
    print(age)
    if age >= 18:
        print('yes, age >= 18')
    else:
        print('no, age < 18')

def task_16(month: int):
    print('\ntask_16')
    print('month', month)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= month <= 12:
        print(days[month]) 
    else:
        print('error in data')

def main():
    task_4(4, 2)
    task_4(3, 2)
    task_8()
    task_10(1, -4, 1.5)  # -1 -3
    task_10(1, 0, 0)  # 0
    task_10(0, 0, 1)  # no answer

    task_15(17)
    task_15(19)

    task_16(0)  # error
    task_16(13)  # error
    task_16(1)  # 31
    task_16(2)  # 28

if __name__ == "__main__":
    main()


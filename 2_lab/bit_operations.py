
def pobit_task_3():
    print("pobit_task_3")
    temp = 2
    temp <<= 5;
    print(temp)

def pobit_task_6(z: int = 0):
    print("\npobit_task_6")
    print(z, bin(z))
    answer = "yes" if z & 1 else "no"
    print(answer)

def pobit_task_7(z: int = 0b1111011):
    print('\npobit_task_7')
    print(z, bin(z))
    z >>= 1
    z <<= 1
    print(z, bin(z))

def pobit_task_15(z: int = 174):
    print('\npobit_task_15')
    print(z, bin(z))
    count_of_bits = 0
    while z > 0:
        count_of_bits += 1
        z >>= 1
    print('count of bits', count_of_bits)

def main():
    pobit_task_3()
    temp = 0b1011010
    pobit_task_6(temp)
    temp = 0b1011011
    pobit_task_6(temp)

    pobit_task_7()

    pobit_task_15()

if __name__ == '__main__':
    main()

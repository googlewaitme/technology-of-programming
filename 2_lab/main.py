def set_task_1():
    print('set_task_1')
    my_tuple = (1, 2, 5, 6, 7, 6, 2, 5)
    print(set(my_tuple))

def set_task_11():
    print('\nset_task_11')
    my_list = [1, 0, 1, 10, 5, 6, 7, 4, 4, 1, 6, 2, 5]

    my_set = set(my_list)

    list_without_equal_elems = list(my_set)

    print(list_without_equal_elems)

def set_task_14_and_15():
    print('\nset_task_14 and 15')
    A = {0, 1, 2, 6, 7, 8, 9}
    B = {1, 3, 6, 10, 9, 21, 5}

    print('A-B=', A-B)
    print('B-A=', B-A)


def main():
    set_task_1()
    set_task_11()
    set_task_14_and_15()


if __name__ == '__main__':
    main()



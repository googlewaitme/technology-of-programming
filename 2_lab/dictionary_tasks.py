def dict_task_5():
    print('dict_task_5')
    my_dict = {1: 10, 'a': 5, 'b': -2}
    print('sum', sum(my_dict.values()))


def dict_task_7():
    print('\ndict_task_7')
    my_dict = {1: 10, 'a': 5, 'b': -2}
    print('old_my_dict', my_dict)
    my_dict['a'] = 10
    print('new_my_dict', my_dict)

def dict_task_11():
    print('\ndict_task_11')
    my_list1 = [1, 2, 3, 4, 9, 7, 4]
    my_list2 = [2, 13, 4, 8, 7, 6]
    my_dict = dict(zip(my_list1, my_list2))
    print(my_dict)

def dict_task_16():
    print('\ndict_task_16')
    my_dict = {'name': 'Alex', 'age':25, 'salary': 8000}
    print(list(my_dict.keys()))


def main():
    dict_task_5()
    dict_task_7()
    dict_task_11()
    dict_task_16()


if __name__ == '__main__':
    main()


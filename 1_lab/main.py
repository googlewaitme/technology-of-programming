# created by Bulat 04.02.2023

def str_task_9():
    print('str 9 task\n')
    str1 = input("input str1: ")
    str2 = input("input str2: ")

    middle_str1 = len(str1) // 2
    middle_str2 = len(str2) // 2


    new_str = "".join(
            [str1[0],
             str2[0],
             str1[middle_str1],
             str2[middle_str2],
             str1[-1],
             str2[-1]]
    )
    print(new_str)

def str_task_10():
    print('\nstr task_10\n')
    string = "Как дела?"    
    print(string[::-1])


def str_task_11():
    print('\nstr_task_11\n')
    string = "В данной главе мы ознакомились с тем, как выполнить установку интерпретатора"
    print(string.split())


def list_task_14():
    print('\nlist_task_14\n')
    my_list = [1, 2, 3]
    print("old_my_list", my_list)
    my_list.insert(0, 12)
    print("my_list", my_list)

def list_task_17():
    print('\nlist_task_17\n')
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2]
    print('my_list is', my_list)
    print('count of 2 in them', my_list.count(2))

def list_task_20():
    print('\nlist_task_20\n')
    my_list = [1, -2, 43, -42, 59, 6, 23]
    print('my_list is', my_list)
    print('6 in my_list:', 6 in my_list)

def list_task_27():
    print('\nlist_task_27\n')
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, 'a', 'b', 2, 5]
    print('my_list is', my_list)
    middle_id = len(my_list) // 2
    new_list = [my_list[0], my_list[middle_id], my_list[-1]]
    print('new_list is', new_list)

def tuple_task_6():
    print('\ntuple_task_6\n')
    my_tuple = (1, 2, 3, 1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2)
    print('my_typle is', my_tuple)
    print('count of 3 in my_typle:', my_tuple.count(3))

def tuple_task_8():
    print('\ntuple_task_8\n')
    my_tuple = (0, -2, 81, 42, 6, -6, 23)
    print('my_tuple is', my_tuple)
    print('min(my_tuple) is', min(my_tuple))

def tuple_task_9():
    print('\ntuple_task_9\n')
    my_tuple = (0, -2, 81, 42, 6, -6, 23)
    print('my_tuple is', my_tuple)
    print('-6 in my_tuple:', -6 in my_tuple)

def tuple_task_16():
    print('\ntuple_task_16\n')
    my_tuple = (1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, 'a', 'b', 2, 5)
    print('my_tuple is', my_tuple)
    print('erased_tuple:', my_tuple[-5:])


def main():
    str_task_9()
    str_task_10()
    str_task_11()
    print('---')

    list_task_14()
    list_task_17()
    list_task_20()
    list_task_27()
    print('---')


    tuple_task_6()
    tuple_task_8()
    tuple_task_9()
    tuple_task_16()

if __name__ == "__main__":
    main()


# Лабораторная работа №6
### Задания на декораторы

- 3. Напишите декоратор upcase_result, который будет переводить все
символы результирующего значения функции reverse_str в верхний
регистр. На вход функции reverse_str подается строка и возвращается
ее инвертированное представление.

- 9. Напишите декоратор time_run, вычисляющий время выполнения
декорируемой функции и возвращающий время выполнения вместо
результата декорируемой функции. В качестве декорируемой
напишите функцию algebraic_sum, на вход которой подается два
значения N и k (по умолчанию равно 2). Функция должна возвращать
результат следующего выражения: $1^k + 2^k + 3^k + ... + N^k$

- 10. Напишите декоратор mul_result с целочисленным аргументом N,
умножающий результат выполнения декорируемой функции на N и
возвращающий полученное значение. В качестве декорируемой
напишите функцию add, вычисляющий сумму двух поступающих на
ее вход значений.

### Задания на генераторы

- 1. Напишите генераторную функцию my_generator, которая позволяет
итерироваться по элементам заданного отрезка с настраиваемым
шагом step (по умолчанию равен 1). При написании данной функции
запрещено использовать стандартную функцию верхнего уровня –
range.
- 3. Напишите генераторную функцию my_enumerate, на вход которой
подается список и она возвращает на каждой итерации кортеж,
состоящий из двух элементов: index – текущий номер индекса
элемента, val – значение, хранящееся по этому индексу. При
написании данной функции запрещено использовать стандартную
функцию верхнего уровня – enumerate.
- 5. Напишите генераторную функцию my_pow, на вход которой подается
целочисленное значение n. На каждом шаге итерации генератор
должен возвращать $n = n^2$.

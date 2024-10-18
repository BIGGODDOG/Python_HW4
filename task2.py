# Задание 2
# Создайте функцию, которая возвращает сумму значений элементов списков. 
# Функция принимает два списка. Используйте механизм генераторов внутри функции. 

# Например, если у нас есть такие списки: 
# 1          3          4          2
# 8          3          5          9

# Результат будет:
# 9          6          9          11 

# Если переданные списки разной длины отсутствующие элементы необходимо считать равными нулю.
from itertools import zip_longest

def sum_of_lists(list1, list2):
    # Используем zip_longest для объединения списков до длины самого длинного, заполняя другой нулями
    for x, y in zip_longest(list1, list2, fillvalue=0):
        yield x + y

print("Case 1:")

list1 = [1, 3, 4, 2]
list2 = [8, 3, 5, 9]

for result in sum_of_lists(list1, list2):
    print(result)

print("\nCase 2:")

list1 = [1, 2, 3, 4, 10]
list2 = [1, 2, 3, 4]

for result in sum_of_lists(list1, list2):
    print(result)
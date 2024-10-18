# Задание 3
# Для решения этой задачи обязательно используйте механизм функций высшего порядка 
# (high order functions). Создайте функцию, которая возводит значения списка в квадрат или в куб. 
# Пользователь определяет, что необходимо сделать (квадрат или куб).

# Сигнатура функции:

# def calculate(list_to_work, function_to_call)

# list_to_work – список c элементами

# function_to_call – функция для модификации значений (функция для возведения 
# значений в квадрат или функция для возведения значений в куб).

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def calculate(list_to_work, function_to_call):
    return list(map(function_to_call, list_to_work))

list_to_work = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print("Square: ")
result = calculate(list_to_work, square)
print(result)

print("Cube: ")
result = calculate(list_to_work, cube)
print(result)
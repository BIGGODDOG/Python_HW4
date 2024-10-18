# Задание 1
# Создайте функцию, которая возвращает все числа Фибоначчи в диапазоне. 
# Функция принимает начало и конец диапазона в качестве параметров. 
# Используйте механизм генераторов внутри функции. 

def fibonacci_in_range(start, end):
    def fibonacci_gen():
        a, b = 0, 1
        while a <= end:
            yield a
            a, b = b, a + b
    
    return [num for num in fibonacci_gen() if num >= start]

start = 10
end = 100
print(fibonacci_in_range(start, end))
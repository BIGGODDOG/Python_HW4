task1.py
Создайте функцию, которая возвращает все числа Фибоначчи в диапазоне. Функция принимает начало и конец диапазона в качестве параметров. Используйте механизм генераторов внутри функции. 


task2.py
Создайте функцию, которая возвращает сумму значений элементов списков. Функция принимает два списка. Используйте механизм генераторов внутри функции. 

Например, если у нас есть такие списки: 
1          3          4          2
8          3          5          9

Результат будет:
9          6          9          11 

Если переданные списки разной длины отсутствующие элементы необходимо считать равными нулю.


task3.py
Для решения этой задачи обязательно используйте механизм функций высшего порядка (high order functions). Создайте функцию, которая возводит значения списка в квадрат или в куб. Пользователь определяет, что необходимо сделать (квадрат или куб).

Сигнатура функции:

def calculate(list_to_work, function_to_call)

list_to_work – список c элементами

function_to_call – функция для модификации значений (функция для возведения значений в квадрат или функция для возведения значений в куб).

 
task4.py
Каждый год ваша компания предоставляет различным государственным организациям финансовую отчетность. В зависимости от организации форматы отчетности разные. Используя механизм декораторов, решите вопрос отчетности для организаций

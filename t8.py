'''
Напишіть програму для обчислення площі та периметра прямокутника.

Молодець, а тепер використайте свій модуль з минулого завдання і 
напишіть програму, яка обчислює спочатку периметр, 
а після - площу прямокутника. Виведіть результат на екран.
'''

# Підключи модуль з попереднього завдання


a = int(input("Введіть першу сторону прямокутника:"))
b = int(input("Введіть другу сторону прямокутника:"))

# Підключення модуля з попереднього завдання
import rectangle_module

# Введення розмірів прямокутника в користувача
a = int(input("Введіть першу сторону прямокутника: "))
b = int(input("Введіть другу сторону прямокутника: "))

# Обчислення периметра за допомогою функції з модуля
perimeter_result = rectangle_module.perimeter(a, b)

# Виведення периметра на екран
print(f"Периметр прямокутника: {perimeter_result}")

# Обчислення площі за допомогою функції з модуля
area_result = rectangle_module.area(a, b)

# Виведення площі на екран
print(f"Площа прямокутника: {area_result}")
'''
Медіана - число, яке ділить ряд чисел на дві рівні частини, 
в одній з яких числа більше медіани, в іншій - менше. 
Давайте напишемо програму, яка виводить медіану трьох чисел!

В основній програмі користувач вводить три числа, 
які передаються в якості параметрів в функцію. 
Функція повинна повернути медіану трьох чисел, 
тобто середнє з цих чисел. 
Наприклад, серед чисел 4, 6, 2 медіаною є число 4. 
Серед чисел 5 4 5 медіаною є 5.
'''
def median(a, b, c):
    # Створюємо список з трьох чисел
    numbers = [a, b, c]
    
    # Сортуємо список за зростанням
    numbers.sort()
    
    # Повертаємо середнє число
    return numbers[1]

# Користувач вводить три числа
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

# Виводимо медіану на екран
print("Медіана трьох чисел:", median(a, b, c))

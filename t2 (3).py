'''
Підключіть модуль і подивіться, в яку пору року і день тижня Ви народилися.
Перед Вами програма, яка використовує функції season 
і day з попередньої програми. 
Підключіть модуль birthday і подивіться, що вийде!
'''

from birthday import season, day

# Програма запитує номер місяця та друкує його назву
m = int(input("Введіть номер місяця Вашого народження: "))
s1 = "Це - " + season(m) + "."
print(s1)
# Програма запитує номер дня тижня та друкує його назву
d = int(input("Введіть номер дня тижня, коли Ви народилися: "))
s2 = "Це - " + day(d) + "."
print(s2)


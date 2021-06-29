'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

n = input('Please, write a number more than 0: ')

while n < '0':
    print(f"The number is less than 0. Please, insert a correct number")
    n = input('Please, write a number more than 0: ')

print(f"Считаем {n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

'''
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
'''

var_num = int(input('Please, insert a positive number: '))
max_digit = 0
num = var_num
while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
        if max_digit == 9:
            break
    num = num // 10

print(f"The greatest digit in {var_num} is {max_digit}")

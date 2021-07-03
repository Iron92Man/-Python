'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

month = int(input("Insert month's number: "))

month_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
              9: 'fall', 10: 'fall', 11: 'fall', 12: 'winter'}

month_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'fall', 'fall', 'fall',
              'winter']

if month in month_dict:
    print(f"{month} belongs to {month_dict[month]}")
    print(f"{month} belongs to {month_list[month - 1]}")
else:
    print("There is no month with such a number")

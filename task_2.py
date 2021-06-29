'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты,
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

time_in_sec = int(input('Please, fill the seconds quantity:'))
hours = time_in_sec // 3600
minutes = (time_in_sec - (hours * 3600)) // 60
seconds = time_in_sec % 60
print(f"The correct time is {hours:02}:{minutes:02}:{seconds:02}")

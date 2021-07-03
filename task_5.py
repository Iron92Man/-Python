'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''

my_rating = [7, 5, 3, 3, 2]
new_number = int(input("Isert a new rating number from 1 to 9: "))
i = 0
if new_number < 10:
    for el in my_rating:
        if new_number <= el:
            i += 1
        else:
            break
    my_rating.insert(i, new_number)
    print(my_rating)
else:
    print("Wrong number!")

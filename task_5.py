'''
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
Выведите соответствующее сообщение.

Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
'''

revenue = int(input("Please, insert your company's revenue for YE2020: "))
expense = int(input("Please, insert your company's expense for YE2020: "))

if revenue > 0:
    if expense > 0:
        print(f"Your profitability is {float((revenue / expense) - 1):.2f}%")
        headcount = int(input("Please, provide me with your company's headcount: "))
        print(f"Your profit per employee is {float(revenue / headcount):.2f}")
    elif expense < 0:
        print(f"Your profitability is {float((revenue / - expense) - 1):.2f}%")
        headcount = int(input("Please, provide me with your company's headcount: "))
        print(f"Your profit per employee is {float(revenue / headcount):.2f}")
    else:
        print(f"Your profitability is 100%")
        headcount = int(input("Please, provide me with your company's headcount: "))
        print(f"Your profit per employee is {float(revenue / headcount):.2f}")
else:
    print(f"Your firm is non-profitable :(")
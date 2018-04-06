# 12. Для проверки остаточных знаний учеников после летних каникул, учитель младших классов решил начинать каждый урок с того,
# чтобы задавать каждому ученику пример из таблицы умножения, но в классе 15 человек, а примеры среди них не должны повторяться.
# В помощь учителю напишите программу, которая будет выводить на экран 15 случайных примеров из таблицы умножения (от 2*2 до 9*9,
# потому что задания по умножению на 1 и на 10 — слишком просты). При этом среди 15 примеров не должно быть повторяющихся
# (примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)

import random
from pprint import pprint as pp

def pupils_test():
    start = 2
    end = 9
    pupils_task = []
    quantity = 15
    expression = ''
    for i in range(quantity):
        num1 = random.randint(start, end)
        num2 = random.randint(start, end)
        if str(num1) and str(num2) in expression:
            continue
        expression = '%d * %d' %(num1, num2)
        pupils_task.append(expression)
    pp(pupils_task)
    return pupils_task

pupils_test()
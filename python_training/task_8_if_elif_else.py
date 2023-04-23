# Программа проверяет является число положительным
# или отрицательным и выводит соответствующее сообщение

num = 3

# Попробовать след значения num
# num = -5
# num = 0

if num >= 0:
    print("число больше либо равно 0")
else:
    print("число отрицательное")

str_1 = "test"
str_2 = "test1"

if str_1 in str_2:
    print("ДА")
else:
    print("Нет")


num_float = - 4.5
# num_float = 0
# num_float = 3.4

if num_float > 0:
    print("положительное число")
elif num_float == 0:
    print("ноль")
else:
    print("число отрицательное")


permit_print = True

if num > 0 and permit_print:
    print("num - положительное число")
elif not permit_print:
    print("печать запрещена")


x = 500
if x > 100 or x < -100:
    print("-")
else:
    print('+')
a = 5 # 2 task
b = 7
if a > b:
    print(a)
else:
    print(b)


# 3 task
c = 10
d = 130
if c - 135 < d < c + 135:
    print("yes")
else:
    print("no")


# 4 task
month = 13

if 0 < month <= 2 or month == 12:
    print("winter")
elif 3 <= month < 6:
    print("весна")
elif 6 <= month < 9:
    print("лето")
elif 9 <= month < 12:
    print("осен")
else:
    print("неверно значение")


# 5 задание
five_a = 20
five_b = 15
five_c = 4

if five_a > 10 and five_b > 10 and five_c > 10:
    print("yes")
else:
    print("no")

# 7 задание
y = 5
z = 11
day = y * 12 * 29 + z * 29
print(day)


# 6 task
summ = 0 # положительные значения
sub = 0 # отрицательные значения
y = 6
u = 4
i = - 5
o = 2
p = 12
if y > 0:
    summ = summ + 1
else:
    sub = sub + 1
if u > 0:
    summ = summ + 1
else:
    sub = sub + 1
if i > 0:
    summ = summ + 1
else:
    sub = sub + 1
if o > 0:
    summ = summ + 1
else:
    sub = sub + 1
if p > 0:
    summ = summ + 1
else:
    sub = sub + 1
print("кол-во положительных значений: ", summ)
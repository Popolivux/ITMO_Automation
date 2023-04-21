def task_1(a: int, b: float, c: str, d: list, e: bool):

    return type(a), type(b), type(c), type(d), type(e)


print(task_1(4, 1.04, "robin", [3, 4, 9 ], 10 < 5))


def task_2(a):

    return a[0:3]  # отображение первых 3 значений списка (числа Фибоначи)


print(task_2([1, 2, 3, 5, 8, 13, 21]))


def task_3(a):
    return a**2


print(task_3(4))
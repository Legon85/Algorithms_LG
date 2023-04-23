def countdown(i):  # countdown
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


countdown(5)


def fact(x):  # factorial
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(5))


def sums(lst):  # sum of digits
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 0:
        return 0
    else:
        return lst[0] + sums(lst[1:])


print(sums([i for i in range(1, 11)]))

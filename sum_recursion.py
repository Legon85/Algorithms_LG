def summa(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0]+summa(arr[1:])


print(summa([7, 9, 4, 3]))

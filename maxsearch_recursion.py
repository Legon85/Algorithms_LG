def maximum(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = maximum(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


digits = [5, 3, 4, 9, 7, 6, 2, 1, 8]

print(maximum(digits))

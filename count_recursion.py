def cnt(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return 1
    else:
        return 1 + cnt(lst[1:])


print(cnt([7, 9, 4, 3]))





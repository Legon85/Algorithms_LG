def selection_sort(lst):
    """O(n**2)"""
    for num in range(len(lst)):
        min_value = num

        for item in range(num, len(lst)):
            if lst[min_value] > lst[item]:  # minimal index search
                min_value = item

        lst[num], lst[min_value] = lst[min_value], lst[num]

    return lst


digits = [5, 3, 4, 9, 7, 6, 2, 1, 8]
print('before:', digits)

result = selection_sort(digits)

print('after:', result)

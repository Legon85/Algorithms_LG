def binary_search(lst, item):
    """O(log n)"""
    low = 0
    high = len(lst)-1

    while low <= high:
        mid = (low+high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lst = list(range(1, 11))
print(lst)

print(binary_search(lst, 7))
print(binary_search(lst, -1))




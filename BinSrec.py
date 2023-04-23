def binary_search(lst, item):
    """O(log n)"""
    low = 0
    high = len(lst)-1

    while low <= high:
        mid = (low+high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            return binary_search(lst[:mid], item)
        else:
            return binary_search(lst[mid+1:], item)
    return None


lst = list(range(1, 11))
print(lst)

print(binary_search(lst, 8))
# print(binary_search(lst, -1))
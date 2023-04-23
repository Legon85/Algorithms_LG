# import random


def quicksort(array):
    """Fast sort (by Hoar) with recursion  O(n*log N)"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # or digits[random.randint(0, len(digits)-1)] for choosing random value
        # pivot = digits[random.randint(0, len(digits) - 1)]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


digits = [5, 3, 4, 9, 7, 6, 2, 1, 8]

print(quicksort(digits))

from array import *


def find_smallest(arr):
    """Selection sort  O(n**2)"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):

        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = array('i', [])
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


my_array = array('i', [5, 3, 4, 9, 7, 6, 2, 1, 8])


print(selection_sort(my_array))



from array import *
"""O(n**2)"""

def selection_sort(arr):
    new_arr = array('i', [])
    for i in range(len(arr)):
        def find_smallest(arr):
            smallest = arr[0]
            smallest_index = 0
            for i in range(1, len(arr)):
                if arr[i] < smallest:
                    smallest = arr[i]
                    smallest_index = i
            return smallest_index

        new_arr.append(arr.pop(find_smallest(arr)))
    return new_arr


my_array = array('i', [5, 3, 4, 9, 7, 6, 2, 1, 8])


print(selection_sort(my_array))
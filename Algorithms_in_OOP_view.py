from pprint import pprint
from collections import deque
from random import sample


# binlist = [i for i in range(1, 11)]
# print(binlist)
# sort_lst = sample(binlist, 10)

# print(sort_lst)


class Algorithms():
    @classmethod
    def binsearch(cls, lst, pivot):
        low = 0
        high = len(lst) - 1
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == pivot:
                return mid
            elif lst[mid] > pivot:
                high = mid - 1
            else:
                low = mid + 1
        return None

    @classmethod
    def selsort(cls, random_lst):
        for i in range(len(random_lst)):
            min_index = i
            for j in range(i + 1, len(random_lst)):
                if random_lst[min_index] > random_lst[j]:
                    min_index = j
            random_lst[min_index], random_lst[i] = random_lst[i], random_lst[min_index]
        return random_lst

    @classmethod
    def quick_sorting(cls, random_lst):
        if len(random_lst) < 2:
            return random_lst
        else:
            pivot = random_lst[0]
            less = [i for i in random_lst if i < pivot]
            greater = [i for i in random_lst if i > pivot]
            return cls.quick_sorting(less) + [pivot] + cls.quick_sorting(greater)

    @classmethod
    def breadth_first_search(cls, graph, name):
        search_que = deque()
        search_que += graph[name]
        searched = []
        while search_que:
            person = search_que.popleft()
            if person not in searched:
                if person[1] == 'h':
                    return f'{person} is a mango seller!'
                else:
                    search_que += graph[person]
                    searched.append(person)
        return False


print(f'{"-" * 20}"Classmethod"{"-" * 20}')
print(Algorithms.binsearch([i for i in range(1, 11)], 8))
print(Algorithms.selsort([6, 4, 8, 9, 2, 1, 7, 3, 5, 10]))
print(Algorithms.quick_sorting([6, 4, 8, 9, 2, 1, 7, 3, 5, 10]))
print(Algorithms.breadth_first_search(
    {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
     "anuj": [], "peggy": [], "thom": [], "jonny": []}, 'you'))


class Algorithms:
    def binsearch(self, lst, pivot):
        low = 0
        high = len(lst) - 1
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == pivot:
                return mid
            elif lst[mid] > pivot:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def selsort(self, random_lst):
        for i in range(len(random_lst)):
            min_index = i
            for j in range(i + 1, len(random_lst)):
                if random_lst[min_index] > random_lst[j]:
                    min_index = j
            random_lst[min_index], random_lst[i] = random_lst[i], random_lst[min_index]
        return random_lst


print(f'{"-" * 20}"Objectmethod"{"-" * 20}')
bs = Algorithms()
print(bs.binsearch([i for i in range(1, 11)], 8))
print(bs.selsort([6, 4, 8, 9, 2, 1, 7, 3, 5, 10]))
print(Algorithms.binsearch(bs, [i for i in range(1, 11)], 8))
print(Algorithms.selsort(bs, [6, 4, 8, 9, 2, 1, 7, 3, 5, 10]))

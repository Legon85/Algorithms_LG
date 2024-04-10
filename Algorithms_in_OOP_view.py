from pprint import pprint
from collections import deque
from random import sample

# binlist = [i for i in range(1, 11)]
# print(binlist)
# sort_lst = sample(binlist, 10)

# print(sort_lst)

class Algorithms():
    def __init__(self):
        self. __setattr__('right_lst', [1, 2, 3, 4, 5, 6])
        self.__setattr__('item', 3)
        self.__setattr__('random_lst', [2, 1, 5, 8, 4, 3])

    def binsearch(self):
        low = 0
        high = len(self.right_lst) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.right_lst[mid] == self.item:
                return mid
            elif self.right_lst[mid] > self.item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def selsort(self):
        for i in range(len(self.random_lst)):
            min_index = i
            for j in range(i + 1, len(self.random_lst)):
                if self.random_lst[min_index] > self.random_lst[j]:
                    min_index = j
            self.random_lst[min_index], self.random_lst[i] = self.random_lst[i], self.random_lst[min_index]
        return self.random_lst


bs = Algorithms()
print(bs.__dict__)
print(bs.selsort())
print(bs.binsearch())


# '''''''''''''''''''''''''''''binsearch'''''''''''''''''''''''''''''''''''''
# class BinSearch:
#     def __init__(self, lst, item):
#         self.lst = lst
#         self.item = item
#
#     def binsearch(self):
#         low = 0
#         high = len(self.lst) - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if self.lst[mid] == self.item:
#                 return mid
#             elif self.lst[mid] > self.item:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return None
#
#
# bs = BinSearch(binlist, 7)
# print(bs.__dict__)
# print(bs.binsearch())

# ''''''''''''''''''''''''''''''''selection sort'''''''''''''''''''''''''''''
# class SelectionSort:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def selsort(self):
#         for i in range(len(self.lst)):
#             min_index = i
#             for j in range(i+1, len(self.lst)):
#                 if self.lst[min_index] > self.lst[j]:
#                     min_index = j
#             self.lst[min_index], self.lst[i] = self.lst[i], self.lst[min_index]
#         return self.lst
#
#
# ss = SelectionSort(sort_lst)
# print(ss.__dict__)
# print(ss.selsort())

# ''''''''''''''''''''''''''''''''recursion'''''''''''''''''''''''''''''''''
# class Recursions:
#     def __init__(self, x, lst):
#         self.x = x
#         self.lst = lst
#
#     def recursion_countdown(self):
#         print(self.x)
#         self.__init__(self.x - 1, self.lst[1:])
#         if self.x == 0:
#             return self.x
#         else:
#             return self.recursion_countdown()
#
#     def rec_fact(self):
#         self.x -= 1
#         if self.x < 2:
#             return self.x
#         else:
#             return self.x * self.rec_fact()
#
#     def rec_sum(self):
#         self.lst = self.lst[1:]
#         if len(self.lst) == 0:
#             return 0
#         elif len(self.lst) < 2:
#             return self.lst[0]
#         else:
#             return self.lst[0] + self.rec_sum()
#
#
# countdown = Recursions(5, binlist)
# # countdown.recursion_countdown()
# recursion_factorial = Recursions(5, binlist)
# # print(recursion_factorial.rec_fact())
# recursion_sum = Recursions(5, binlist)
#
#
# # print(recursion_sum.rec_sum())
#
# # '''''''''''''''''''''''''''''''quicksort''''''''''''''''''''''''''''''''''
#
# class QuickS:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def sorting(self):
#         if len(self.lst) < 2:
#             return self.lst
#         else:
#             pivot = self.lst[0]
#             less = [i for i in self.lst if i < pivot]
#             greater = [i for i in self.lst if i > pivot]
#             return quicksort.sorting(less) + [pivot] + quicksort.sorting(greater)
#
#
# quicksort = QuickS(sort_lst)
# # print(quicksort.sorting())
#
#
# # ''''''''''''''''''''''''''''breadth_first_search'''''''''''''''''''''''''''
# graph = {"you": ["alice", "bob", "claire"],
#          "bob": ["anuj", "peggy"],
#          "alice": ["peggy"],
#          "claire": ["thom", "jonny"],
#          "anuj": [], "peggy": [], "thom": [], "jonny": []}
#
#
# class BFS:
#     def __init__(self, graph, name):
#         self.graph = graph
#         self.name = name
#
#     # @staticmethod
#     def is_seller(self, person):
#         return person[0] == 'p'
#
#     def b_first_search(self):
#         search_que = deque()
#         search_que += graph[self.name]
#         searched = []
#         while search_que:
#             person = search_que.popleft()
#             if self.is_seller(person) and person not in searched:
#                 return f'{person}  is a mango seller!'
#             else:
#                 search_que += graph[person]
#                 searched.append(person)
#         return False
#
#
# bfs = BFS(graph, "you")
# # print(bfs.b_first_search())
#
# # ''''''''''''''''''''''''''''''Dijkstra''''''''''''''''''''''''''''''''''''
# graf = {"start": {"a": 6, "b": 2},
#         "a": {"fin": 1},
#         "b": {"a": 3, "fin": 5},
#         "fin": {}}
# costs = {"a": 6, "b": 2, "fin": float('inf')}
# parents = {"a": "start", "b": "start", "fin": None}
#
#
# class DIJKSTRA:
#     def __init__(self, graf, costs, parents, processed=[]):
#         self.graf = graf
#         self.costs = costs
#         self.parents = parents
#         self.processed = processed
#
#     def find_lowest_cost_node(self):
#         lowest_cost = float('inf')
#         lowest_cost_node = None
#         for node in self.costs:
#             if self.costs[node] < lowest_cost and node not in self.processed:
#                 lowest_cost = self.costs[node]
#                 lowest_cost_node = node
#         return lowest_cost_node
#
#     def dijkstra_search(self):
#         node = self.find_lowest_cost_node()
#         while node is not None:
#             neighbors = graf[node]
#             for n in neighbors:
#                 new_cost = self.costs[node] + neighbors[n]
#                 if new_cost < self.costs[n]:
#                     self.costs[n] = new_cost
#                     self.parents[n] = node
#             self.processed.append(node)
#             node = self.find_lowest_cost_node()
#
#         print(costs)
#         print(parents)
#         print(self.processed)
#
#
# dij = DIJKSTRA(graf, costs, parents, )
# # dij.dijkstra_search()
#
#
# # ''''''''''''''''''''''''the_set_covering_task'''''''''''''''''''''''''''''
#
# states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
#
# stations = {"kone": {"id", "nv", "ut"},
#             "ktwo": {"wa", "id", "mt"},
#             "kthree": {"or", "nv", "ca"},
#             "kfour": {"nv", "ut"},
#             "kfive": {"ca", "az"}}
#
#
# class SetCover:
#     def __init__(self, states_needed, stations):
#         self.states_needed = states_needed
#         self.stations = stations
#
#     def set_covering_solution(self):
#         final_stations = set()
#         while self.states_needed:
#             best_station = None
#             states_covered = set()
#             for self.station, self.states_for_station in self.stations.items():
#                 covered = self.states_needed & self.states_for_station
#                 if len(covered) > len(states_covered):
#                     best_station = self.station
#                     states_covered = covered
#             final_stations.add(best_station)
#             self.states_needed -= states_covered
#         return final_stations
#
#
# set_cov = SetCover(states_needed, stations)
# # print(set_cov.set_covering_solution())
#
# # ''''''''''''''''''''''''longest_common_substring''''''''''''''''''''''''''''
# dp_table_blue = ['b', 'l', 'u', 'e']
# dp_table_clues = ['c', 'l', 'u', 'e', 's']
#
# class DP_TAB:
#     def __init__(self, blue, clues):
#         self.dp_table_blue = blue
#         self.dp_table_clues = clues
#
#     def substring(self):
#         dp_table = [[0 for i in range(len(self.dp_table_blue))]for i in range(len(self.dp_table_clues))]
#         for i in range(len(self.dp_table_blue)):
#             for j in range(len(self.dp_table_clues)):
#                 if self.dp_table_blue[i] == self.dp_table_clues[j]:
#                     dp_table[j][i] = dp_table[j-1][i-1] + 1
#                 else:
#                     dp_table[j][i] = 0
#         pprint(dp_table, width=15)
#
#
# dp_tab = DP_TAB(dp_table_blue, dp_table_clues)
# dp_tab.substring()
# # ''''''''''''''''''''''''longest_common_subsequence''''''''''''''''''''''''''''
# dp_table_blue = ['b', 'l', 'u', 'e']
# dp_table_clues = ['c', 'l', 'u', 'e', 's']
# class DP_TAB:
#     def __init__(self, blue, clues):
#         self.dp_table_blue = blue
#         self.dp_table_clues = clues
#
#     def substring(self):
#         dp_table = [[0 for i in range(len(self.dp_table_blue))]for i in range(len(self.dp_table_clues))]
#         for i in range(len(self.dp_table_blue)):
#             for j in range(len(self.dp_table_clues)):
#                 if self.dp_table_blue[i] == self.dp_table_clues[j]:
#                     dp_table[j][i] = dp_table[j-1][i-1] + 1
#                 else:
#                     dp_table[j][i] = max(dp_table[j-1][i], dp_table[j][i-1])
#         pprint(dp_table, width=15)
#
#
# dp_tab = DP_TAB(dp_table_blue, dp_table_clues)
# dp_tab.substring()


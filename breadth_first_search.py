from time_test_module import time_test
from collections import deque
"""O(V+E) v - vertecies, E - edges """

graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []}


# @time_test
# def search(name):
#     search_que = deque()
#     search_que += graph[name]
#     searched = []
#     while search_que:
#         person = search_que.popleft()
#         if person not in searched:
#             if person_is_seller(person):
#                 return f'{person} is a mango seller!'
#             else:
#                 search_que += graph[person]
#                 searched.append(person)
#     return False
#
#
# def person_is_seller(person):
#     return person[1] == 'h'
#
#
# print(search("you"))

def search(name):
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


# def person_is_seller(person):
#     return person[1] == 'h'


print(search("you"))
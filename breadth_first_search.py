from time_test_module import time_test
from collections import deque
"""O(V+E) v - vertecies, E - edges """

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


@time_test
def search(name):
    search_que = deque()
    search_que += graph[name]
    searched = []
    while search_que:
        person = search_que.popleft()
        if person not in searched:
            if person_is_seller(person):
                return f'{person} is a mango seller!'
            else:
                search_que += graph[person]
                searched.append(person)
    return False


def person_is_seller(person):
    return person[1] == 'h'


print(search("you"))

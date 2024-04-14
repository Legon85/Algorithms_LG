class Algorithms:
    """Класс алгоритмов определённый под использование объектами класса на основе @staticmethod"""
    @staticmethod
    def binsearch(lst, pivot):
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

    @staticmethod
    def selsort(random_lst):
        for i in range(len(random_lst)):
            min_index = i
            for j in range(i + 1, len(random_lst)):
                if random_lst[min_index] > random_lst[j]:
                    min_index = j
            random_lst[min_index], random_lst[i] = random_lst[i], random_lst[min_index]
        return random_lst

    @staticmethod
    def quick_sorting(random_lst):
        if len(random_lst) < 2:
            return random_lst
        else:
            pivot = random_lst[0]
            less = [i for i in random_lst if i < pivot]
            greater = [i for i in random_lst if i > pivot]
            return Algorithms.quick_sorting(less) + [pivot] + Algorithms.quick_sorting(greater)

    @staticmethod
    def dijkstras_algorithm(graph, costs, parents):
        processed = []

        def find_lowest_cost_node(costs):
            lowest_cost = float("inf")
            lowest_cost_node = None
            for node in costs:
                cost = costs[node]
                if cost < lowest_cost and node not in processed:
                    lowest_cost = cost
                    lowest_cost_node = node
            return lowest_cost_node

        chosen_node = find_lowest_cost_node(costs)
        while chosen_node is not None:
            cost = costs[chosen_node]
            neighbors = graph[chosen_node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]

                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = chosen_node
            processed.append(chosen_node)
            chosen_node = find_lowest_cost_node(costs)

        return costs, parents, processed


if __name__ == '__main__':
    print(f'{"-" * 20}"Objectmethod"{"-" * 20}')
    bs = Algorithms()
    print(bs.__dict__)
    print(Algorithms.__dict__)
    print(bs.binsearch([i for i in range(1, 11)], 8))
    print(bs.selsort([6, 4, 8, 9, 2, 1, 7, 3, 5, 10]))
    print(bs.quick_sorting([6, 4, 8, 9, 2, 1, 7, 3, 5, 10]))
    print(bs.dijkstras_algorithm({"start": {"a": 6,
                                            "b": 2},
                                  "a": {"fin": 1},
                                  "b": {"a": 3,
                                        "fin": 5},
                                  "fin": {}},
                                 {"a": 6,
                                  "b": 2,
                                  "fin": float("inf")},
                                 {"a": "start",
                                  "b": "start",
                                  "fin": None},
                                 ))

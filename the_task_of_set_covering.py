class StatesCovering:
    def __init__(self, states_needed, stations):
        self.states_needed = states_needed
        self.stations = stations

    def set_data(self, states_needed, stations):
        self.states_needed = states_needed
        self.stations = stations

    def set_covering_solution(self):
        final_stations = set()

        while self.states_needed:
            best_station = None
            states_covered = set()
            for station, states_for_station in self.stations.items():
                covered = self.states_needed & states_for_station
                if len(covered) > len(states_covered):
                    best_station = station
                    states_covered = covered
            final_stations.add(best_station)
            self.states_needed -= states_covered
        return final_stations




a = StatesCovering({"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}, {"kone": {"id", "nv", "ut"},
                    "ktwo": {"wa", "id", "mt"},
                    "kthree": {"or", "nv", "ca"},
                    "kfour": {"nv", "ut"},
                    "kfive": {"ca", "az"}})
b = StatesCovering({"mt", "wa", "or", "id", "nv", "ut"}, {"kten": {"id", "nv", "ut"},
                    "ksix": {"wa", "id", "mt"},
                    "kseven": {"or", "nv"},
                    "keight": {"nv", "ut", "id", "mt"},
                    "knine": {"ca", "az"}})
# print(a.__dict__)
print(a.set_covering_solution())
print(b.set_covering_solution())
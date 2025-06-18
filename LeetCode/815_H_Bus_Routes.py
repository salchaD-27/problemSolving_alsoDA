# from typing import List
# class Solution:
#     def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
#         routeBuses={}
#         for i in range(len(routes)):
#             for j in range(len(routes[i])):
#                 if routes[i][j] not in routeBuses: routeBuses[routes[i][j]]=[i]
#                 else: routeBuses[routes[i][j]].append(i)
#         count=float('inf')
#         queue=[]
#         for i in range(len(routes)):
#             if source in routes[i]: queue.append([source, i, 1])
#         if not queue: return -1
#         while queue:
#             currStat, currBus, totalBuses=queue.pop(0)
#             if currStat==target: count=min(count,totalBuses)
#             if totalBuses>count: continue
#             possibleBuses=routeBuses[currStat]
#             for i in range(len(possibleBuses)):
#                 if possibleBuses[i]!=currBus: queue.append([currStat, possibleBuses[i], totalBuses+1])
#             for i in range(len(routes[currBus])):
#                 if routes[currBus][i]!=currStat: queue.append([routes[currBus][i], currBus, totalBuses])
#         return count

from typing import List
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        visited_stops = set()
        visited_routes = set()
        queue = deque()
        for route in stop_to_routes[source]:
            queue.append((route, 1))
            visited_routes.add(route)
        while queue:
            route_index, buses_taken = queue.popleft()
            for stop in routes[route_index]:
                if stop == target: return buses_taken
                if stop in visited_stops: continue
                visited_stops.add(stop)
                for next_route in stop_to_routes[stop]:
                    if next_route not in visited_routes:
                        queue.append((next_route, buses_taken + 1))
                        visited_routes.add(next_route)
        return -1
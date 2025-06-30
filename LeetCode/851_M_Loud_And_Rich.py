# from typing import List
# from collections import deque
# class Solution:
#     def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
#         moreRicher = {}
#         for rich, poor in richer:
#             if poor not in moreRicher: moreRicher[poor] = [rich]
#             else: moreRicher[poor].append(rich)
#         all_richer_bfs = {}
#         for person in range(len(richer)+1):
#             visited = set()
#             queue = deque()
#             if person in moreRicher:
#                 for rich in moreRicher[person]:
#                     queue.append(rich)
#                     visited.add(rich)
#             while queue:
#                 current = queue.popleft()
#                 if current in moreRicher:
#                     for richer_person in moreRicher[current]:
#                         if richer_person not in visited:
#                             visited.add(richer_person)
#                             queue.append(richer_person)
#             all_richer_bfs[person] = visited
#         res=[i for i in range(len(quiet))]
#         for i in range(len(res)):
#             tempMin=quiet[i]
#             for person in all_richer_bfs[i]:
#                 if quiet[person]<tempMin:
#                     tempMin=quiet[person]
#                     res[i]=person
#         return res

from typing import List
from collections import deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        moreRicher = {}
        for rich, poor in richer:
            if poor not in moreRicher: moreRicher[poor] = [rich]
            else: moreRicher[poor].append(rich)
        all_richer_bfs = {}
        for person in range(n):
            visited = set()
            queue = deque()
            if person in moreRicher:
                for rich in moreRicher[person]:
                    queue.append(rich)
                    visited.add(rich)
            while queue:
                current = queue.popleft()
                if current in moreRicher:
                    for richer_person in moreRicher[current]:
                        if richer_person not in visited:
                            visited.add(richer_person)
                            queue.append(richer_person)
            all_richer_bfs[person] = visited
        res = [i for i in range(n)]
        for i in range(n):
            min_person = i
            for person in all_richer_bfs[i]:
                if quiet[person] < quiet[min_person]: min_person = person
            res[i] = min_person
        return res
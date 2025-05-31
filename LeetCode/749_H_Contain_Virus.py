from typing import List
# from collections import deque
# class Solution:
#     def containVirus(self, isInfected: List[List[int]]) -> int:
#         rows, cols = len(isInfected), len(isInfected[0])
#         total_walls = 0
#         directions = [(-1,0), (1,0), (0,-1), (0,1)]
#         def get_regions():
#             visited = [[False]*cols for _ in range(rows)]
#             regions = []
#             for r in range(rows):
#                 for c in range(cols):
#                     if isInfected[r][c] == 1 and not visited[r][c]:
#                         queue = deque()
#                         queue.append((r,c))
#                         region = []
#                         frontier = set()
#                         walls = 0
#                         while queue:
#                             x, y = queue.popleft()
#                             if visited[x][y]: continue
#                             visited[x][y] = True
#                             region.append((x, y))
#                             for dx, dy in directions:
#                                 nx, ny = x + dx, y + dy
#                                 if 0 <= nx < rows and 0 <= ny < cols:
#                                     if isInfected[nx][ny] == 0:
#                                         frontier.add((nx, ny))
#                                         walls += 1
#                                     elif isInfected[nx][ny] == 1 and not visited[nx][ny]: queue.append((nx, ny))
#                         regions.append((region, frontier, walls))
#             return regions

#         while True:
#             regions = get_regions()
#             if not regions: break
#             # largest region
#             regions.sort(key=lambda x: len(x[1]), reverse=True)
#             most_threatening = regions[0]
#             if not most_threatening[1]: break
#             # walls around most threatening region
#             total_walls += most_threatening[2]
#             for x, y in most_threatening[0]:
#                 isInfected[x][y] = -1  # contained
#             # spreading other regions
#             for region, frontier, _ in regions[1:]:
#                 for x, y in frontier:
#                     isInfected[x][y] = 1
#         return total_walls

from typing import List
from collections import deque
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        rows, cols = len(isInfected), len(isInfected[0])
        boundaries = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def calculateRegions():
            visited = [[False] * cols for _ in range(rows)]
            regions = []
            for r in range(rows):
                for c in range(cols):
                    if isInfected[r][c] == 1 and not visited[r][c]:
                        queue = deque()
                        queue.append((r, c))
                        visited[r][c] = True
                        region = [(r, c)]
                        frontier = set()
                        walls = 0
                        while queue:
                            x, y = queue.popleft()
                            for dx, dy in directions:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < rows and 0 <= ny < cols:
                                    if isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        walls += 1
                                    elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        queue.append((nx, ny))
                                        region.append((nx, ny))
                        regions.append((region, frontier, walls))
            return regions

        while True:
            reg = calculateRegions()
            if not reg: break
            reg.sort(key=lambda x: len(x[1]), reverse=True)
            region_to_bound, _, walls = reg[0]
            for r, c in region_to_bound:
                isInfected[r][c] = -1
            boundaries += walls
            for region, frontier, _ in reg[1:]:
                for r, c in frontier:
                    if isInfected[r][c] == 0: isInfected[r][c] = 1
        return boundaries
from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, maxDist = 0, 0, 0
        currDir = 'N'
        leftOf = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        rightOf = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        dirMap = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        obstacleSet = set(map(tuple, obstacles))
        for cmd in commands:
            if cmd == -1: currDir = rightOf[currDir]
            elif cmd == -2: currDir = leftOf[currDir]
            else:
                dx, dy = dirMap[currDir]
                for _ in range(cmd):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacleSet: break
                    x, y = next_x, next_y
                    maxDist = max(maxDist, x * x + y * y)
        return maxDist
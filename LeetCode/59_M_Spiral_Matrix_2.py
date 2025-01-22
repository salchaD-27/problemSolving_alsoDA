from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direcIndex = 0

        topBound = 0
        rightBound = n
        bottomBound = n
        leftBound = 0
        x, y = 0, 0
        currentNum = 1
        while currentNum <= n * n:
            matrix[x][y] = currentNum
            currentNum += 1
            nx, ny = x + direction[direcIndex][0], y + direction[direcIndex][1]
            if nx < topBound or nx >= bottomBound or ny < leftBound or ny >= rightBound or matrix[nx][ny] != 0:
                if direcIndex == 0: topBound += 1
                elif direcIndex == 1: rightBound -= 1
                elif direcIndex == 2: bottomBound -= 1
                elif direcIndex == 3: leftBound += 1
                direcIndex = (direcIndex + 1) % 4  
            x += direction[direcIndex][0]
            y += direction[direcIndex][1]
        return matrix
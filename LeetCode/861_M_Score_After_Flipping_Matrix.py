from typing import List

class Solution:
    def binary(self, row: List[int]) -> int:
        num = 0
        for i, j in enumerate(row):
            num += j * (2 ** (len(row) - i - 1))
        return num

    def matSum(self, grid: List[List[int]]) -> int:
        total = 0
        for row in grid:
            total += self.binary(row)
        return total

    def toggleRow(self, row: List[int]) -> None:
        for i in range(len(row)):
            row[i] = 1 - row[i]

    def toggleCol(self, grid: List[List[int]], colNum: int) -> None:
        for i in range(len(grid)):
            grid[i][colNum] = 1 - grid[i][colNum]

    def matrixScore(self, grid: List[List[int]]) -> int:
        score = self.matSum(grid)
        max_iterations = 3

        for _ in range(max_iterations):
            for row in grid:
                self.toggleRow(row)
                tempScore = self.matSum(grid)
                if tempScore > score:
                    score = tempScore
                else:
                    self.toggleRow(row)

            colSize = len(grid[0])
            for i in range(colSize):
                self.toggleCol(grid, i)
                tempScore = self.matSum(grid)
                if tempScore > score:
                    score = tempScore
                else:
                    self.toggleCol(grid, i)

        return score

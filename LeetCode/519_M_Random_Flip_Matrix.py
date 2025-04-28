# import random
# from typing import List
# class Solution:
#     def __init__(self, m: int, n: int):
#         self.grid=[[0]*n for _ in range(m)]
#     def flip(self) -> List[int]:
#         i=random.randint(0, len(self.grid)-1)
#         j=random.randint(0, len(self.grid[0])-1)
#         self.grid[i][j]=1
#         return [i,j]
#     def reset(self) -> None:
#         for i in range(len(self.grid)):
#             for j in range(len(self.grid[i])):
#                 self.grid[i][j]=0

# import random
# from typing import List
# class Solution:
#     def __init__(self, m: int, n: int):
#         self.m = m  
#         self.n = n  
#         self.grid = [[0] * n for _ in range(m)]  
#         self.available = [(i, j) for i in range(m) for j in range(n)]
#     def flip(self) -> List[int]:
#         i, j = random.choice(self.available)
#         self.grid[i][j] = 1
#         self.available.remove((i, j))
#         return [i, j]
#     def reset(self) -> None:
#         self.grid = [[0] * self.n for _ in range(self.m)]
#         self.available = [(i, j) for i in range(self.m) for j in range(self.n)]

import random
from typing import List
class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.flipped = set()
    def flip(self) -> List[int]:
        while True:
            i = random.randint(0, self.m - 1)
            j = random.randint(0, self.n - 1)
            if (i, j) not in self.flipped:
                self.flipped.add((i, j))
                return [i, j]
    def reset(self) -> None:
        self.flipped.clear()
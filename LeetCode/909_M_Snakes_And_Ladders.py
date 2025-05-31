# from typing import List
# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#         n = len(board)
#         steps = float('inf')
#         visited = set()
#         def getRC(square: int) -> tuple[int, int]:
#             quot, rem = divmod(square - 1, n)
#             row = n - 1 - quot
#             col = rem if (n - 1 - row) % 2 == 0 else n - 1 - rem
#             return row, col
#         def getSquare(r: int, c: int) -> int:
#             rowFromBottom = n - 1 - r
#             if rowFromBottom % 2 == 0: return rowFromBottom * n + c + 1
#             else: return rowFromBottom * n + (n - 1 - c) + 1
#         def next6MoveRCs(r: int, c: int) -> List[tuple[int, int]]:
#             currSquare = getSquare(r, c)
#             res = []
#             for i in range(1, 7):
#                 if currSquare + i > n * n: break
#                 res.append(getRC(currSquare + i))
#             return res
#         def fs(currSteps: int, r: int, c: int):
#             nonlocal steps
#             square = getSquare(r, c)
#             if (r, c) in visited: return
#             visited.add((r, c))
#             if square == n * n:
#                 steps = min(steps, currSteps)
#                 visited.remove((r, c))
#                 return
#             if currSteps >= steps:
#                 visited.remove((r, c))
#                 return
#             for nr, nc in next6MoveRCs(r, c):
#                 if board[nr][nc] == -1: fs(currSteps + 1, nr, nc)
#                 else:
#                     tr, tc = getRC(board[nr][nc])
#                     fs(currSteps + 1, tr, tc)
#             visited.remove((r, c))

#         fs(0, n - 1, 0)
#         return steps if steps != float('inf') else -1
    
from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_rc(square: int) -> tuple[int, int]:
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot
            col = rem if (n - 1 - row) % 2 == 0 else n - 1 - rem
            return row, col
        visited = set()
        queue = deque([(1, 0)])  # square,steps
        while queue:
            square, steps = queue.popleft()
            if square == n * n: return steps
            for move in range(1, 7):
                next_square = square + move
                if next_square > n * n: continue
                r, c = get_rc(next_square)
                if board[r][c] != -1: next_square = board[r][c]
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, steps + 1))
        return -1
# from typing import List
# class Solution:
#     def pathsWithMaxScore(self, board: List[str]) -> List[int]:
#         MOD = 10**9 + 7
#         inf=float('inf')
#         m, n = len(board), len(board[0])
#         def dfs(i: int, j: int) -> tuple:
#             if i < 0 or j < 0 or board[i][j] == 'X': return (-inf, 0)
#             if i == 0 and j == 0: return (0, 1)

#             score = int(board[i][j]) if board[i][j].isdigit() else 0
#             best = -inf
#             ways = 0
#             for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
#                 new_i, new_j = i + di, j + dj
#                 s, w = dfs(new_i, new_j)
#                 if s > best:
#                     best = s
#                     ways = w
#                 elif s == best: ways += w
#             return (best + score, ways)
#         s, w = dfs(m - 1, n - 1)
#         return [max(s, 0), w % MOD]

from typing import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        inf=float('inf')
        m, n = len(board), len(board[0])
        f = [[-inf] * (n + 1) for _ in range(m + 1)] # f: best score
        g = [[0] * (n + 1) for _ in range(m + 1)] # g: ways
        f[1][1] = 0
        g[1][1] = 1
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or board[i][j] == 'X':
                    continue
                score = int(board[i][j]) if board[i][j].isdigit() else 0
                best = -inf
                ways = 0
                for di, dj in [(0, 1), (1, 0), (0, 0)]:
                    new_i, new_j = i + di, j + dj
                    s = f[new_i][new_j]
                    w = g[new_i][new_j]

                    if s > best:
                        best = s
                        ways = w
                    elif s == best:
                        ways += w
                f[i + 1][j + 1] = best + score
                g[i + 1][j + 1] = ways
        s, w = f[m][n], g[m][n]
        return [max(s, 0), w % MOD]
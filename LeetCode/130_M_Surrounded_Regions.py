from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != 'O': return
            board[x][y] = 'T'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        if not board or not board[0]: return
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][cols-1] == 'O': dfs(i, cols-1)
        for j in range(cols):
            if board[0][j] == 'O': dfs(0, j)
            if board[rows-1][j] == 'O': dfs(rows-1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O': board[i][j] = 'X' 
                elif board[i][j] == 'T': board[i][j] = 'O'
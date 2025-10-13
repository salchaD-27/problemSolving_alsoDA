# class Solution:
#     def alphabetBoardPath(self, target: str) -> str:
#         m = {c: [i / 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
#         x0, y0 = 0, 0
#         res = []
#         for c in target:
#             x, y = m[c]
#             if y < y0: res.append('L' * (y0 - y))
#             if x < x0: res.append('U' * (x0 - x))
#             if x > x0: res.append('D' * (x - x0))
#             if y > y0: res.append('R' * (y - y0))
#             res.append('!')
#             x0, y0 = x, y
#         return "".join(res)

from collections import deque
class Solution(object):
    def alphabetBoardPath(self, target):
        res=[]
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        def bfs(x,y,target):
            if board[x][y]==target:
                return x,y,'!'
            q=deque([(x,y,"")])
            visited={(x,y)}
            while q:
                x,y,path=q.popleft()
                for i,j,s in [(1,0,'D'),(0,1,'R'),(-1,0,'U'),(0,-1,'L')]:
                    if 0<=x+i<=5 and 0<=y+j<len(board[x+i]) and (x+i,y+j) not in visited:
                        visited.add((x+i,y+j))
                        if board[x+i][y+j]==target: return x+i,y+j,path+s+'!'
                        else: q.append((x+i,y+j,path+s))
        x,y=0,0
        for ch in target:
            x,y,path=bfs(x,y,ch)
            res.append(path)
        return ''.join(res)
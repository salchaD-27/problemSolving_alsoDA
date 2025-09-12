from typing import List
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j]==1:
                        q.append((i,j))
                        vis[i][j]=1
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                row,col=r+dr,c+dc
                if 0<=row<n and 0<=col<m and not vis[row][col] and grid[row][col]==1:
                    vis[row][col]=1
                    q.append((row,col))
        ans=0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j]==1: ans+=1
        return ans
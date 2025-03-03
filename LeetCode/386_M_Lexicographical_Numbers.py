class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[str(i) for i in range(1, n+1)]
        res.sort()
        res=[int(char) for char in res]
        return res

from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur):
            if cur>n: return
            res.append(cur)
            for i in range(10):
                dfs(cur*10 + i)
        res = []
        for i in range(1, 10):
            dfs(i)
        return res
    
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        cur = 1
        while len(res)<n:
            res.append(cur)
            if cur*10 <= n: cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur = cur // 10
                cur += 1
        return res
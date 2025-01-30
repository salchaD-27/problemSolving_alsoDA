# from typing import List
# class Solution:
#     def minCut(self, s: str) -> int:
#         def is_palindrome(str): return str == str[::-1]
#         def backtrack(start: int, path: List[str]):
#             if start == len(s):
#                 ans.append(path[:])
#                 return
#             for end in range(start, len(s)): 
#                 if is_palindrome(s[start:end+1]): 
#                     path.append(s[start:end+1]) 
#                     backtrack(end+1, path) 
#                     path.pop()  
        
#         ans = []
#         backtrack(0, [])
#         minAns=len(ans[0])
#         for pal in ans:
#             minAns=min(minAns, len(pal))
#         return minAns-1


from typing import List
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or palindrome[start + 1][end - 1]): palindrome[start][end] = True

        dp = [float('inf')] * n
        for i in range(n):
            if palindrome[0][i]: dp[i] = 0
            else:
                for j in range(i): 
                    if palindrome[j + 1][i]: dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]
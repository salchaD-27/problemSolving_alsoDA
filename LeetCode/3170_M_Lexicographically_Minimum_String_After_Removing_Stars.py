# class Solution:
#     def clearStars(self, s: str) -> str:
#         stack = []
#         for char in s:
#             if char == '*': stack.pop()
#             else: stack.append(char)
#         return ''.join(stack)

# class Solution:
#     def clearStars(self, s: str) -> str:
#         stack = []
#         for char in s:
#             if char == '*': stack.pop()
#             else: stack.append(char)
#         return ''.join(stack)

import heapq
from collections import defaultdict, deque
class Solution(object):
    def clearStars(self, s):
        n = len(s)
        pq = []  
        m = defaultdict(deque) 
        keep = [True] * n 
        for i in range(n):
            if s[i] == '*':
                smallest = heapq.heappop(pq)
                idx = m[smallest].pop()    
                keep[i] = False            
                keep[idx] = False          
            else:
                heapq.heappush(pq, s[i])
                m[s[i]].append(i)
        return ''.join(s[i] for i in range(n) if keep[i])
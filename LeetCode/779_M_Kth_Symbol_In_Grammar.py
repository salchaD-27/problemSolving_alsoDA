# class Solution:
#     def kthGrammar(self, n: int, k: int) -> int:
#         second=False
#         if k%2==0: second=True
#         def fs(n, k):
#             if n==1: return 0
#             if n==2: return 0 if k==0 else 1
#             if second: return 0 if fs(n-1, k//2)==1 else 1
#             else: return 1 if fs(n-1, (k+1)//2)==1 else 0
#         if second: return 0 if fs(n, k)==1 else 1
#         else: return 1 if fs(n, k)==1 else 0

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        if k % 2 == 1: return parent
        else: return 1 - parent
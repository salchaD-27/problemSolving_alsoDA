# 65786543
# 65 78 6543
# 65 87 6543
# 65 8 76543
# 65 8 34567
# 65834567

# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         def reverse(str): return str[::-1]
#         n=str(n)
#         res=''
#         flag=False
#         for i in range(len(str(n))-1,0,-1):
#             if(n[i]>n[i-1]):
#                 res=n[:i-1]+n[i]+reverse(n[i+1:])+n[i-1]
#                 flag=True
#                 break
#         return int(res) if (flag and int(res)<=2**31-1) else -1
    
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        i = len(n) - 2
        while i >= 0 and n[i] >= n[i + 1]:
            i -= 1
        if i == -1: return -1
        j = len(n) - 1
        while n[j] <= n[i]:
            j -= 1
        n[i], n[j] = n[j], n[i]
        n = n[:i+1] + sorted(n[i+1:])
        result = int(''.join(n))
        return result if result <= 2**31 - 1 else -1
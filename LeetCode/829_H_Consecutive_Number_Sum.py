# class Solution:
#     def consecutiveNumbersSum(self, n: int) -> int:
#         def poss(i):
#             target=n
#             while target>0:
#                 target-=i
#                 i+=1
#             return target==0
#         count=0
#         for i in range(1, n//2+1):
#             if poss(i): count+=1
#         return count

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        k = 1
        while k * (k - 1) // 2 < n:
            if (n - k * (k - 1) // 2) % k == 0: count += 1
            k += 1
        return count
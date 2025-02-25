# class Solution:
#     def countNumbersWithUniqueDigits(self, n: int) -> int:
#         count=1
#         x=1
#         while(x<10**n):
#             x+=10
#             count+=9
#         return count
    
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        
        total = 10
        unique_digits = 9
        available = 9
        for i in range(2, n + 1):
            unique_digits *= available
            total += unique_digits
            available -= 1
        return total
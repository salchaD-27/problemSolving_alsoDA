# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         while n>1:
#             n=n//3
#         return True if n==1 else False

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        while n % 3 == 0:
            n //= 3
        return n == 1
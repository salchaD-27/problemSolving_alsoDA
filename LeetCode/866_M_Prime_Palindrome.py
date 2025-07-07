# class Solution:
#     def primePalindrome(self, n: int) -> int:
#         def isPrime(n):
#             if n <= 1: return False
#             if n <= 3: return True
#             if n % 2 == 0 or n % 3 == 0: return False
#             i = 5
#             while i * i <= n:
#                 if n % i == 0 or n % (i + 2) == 0: return False
#                 i += 6
#             return True
#         while(True):
#             if isPrime(n) and str(n)==str(n)[::-1]: return n
#             n+=1

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_palindrome(x): return str(x) == str(x)[::-1]
        def is_prime(x):
            if x < 2: return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0: return False
            return True
        while True:
            if is_palindrome(n) and is_prime(n): return n
            n += 1
            if 10**7 < n < 10**8: n = 10**8
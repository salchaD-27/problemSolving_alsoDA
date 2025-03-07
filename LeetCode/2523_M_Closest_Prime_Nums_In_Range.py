# import math
# from typing import List
# class Solution:
#     def closestPrimes(self, left: int, right: int) -> List[int]:
#         def isprime(n: int) -> bool:
#             if n <= 1: return False
#             if n <= 3: return True
#             if n % 2 == 0 or n % 3 == 0: return False
#             limit = int(math.sqrt(n))
#             i = 5
#             while i <= limit:
#                 if n % i == 0 or n % (i + 2) == 0: return False
#                 i += 6
#             return True
        
#         i=left
#         while(not isprime(i) and i<=right): i+=1
#         a=i
#         i+=1
#         while(not isprime(i) and i<=right): i+=1
#         b=i
#         if(i>right): return [-1,-1]
#         else: return [a,b]

# import math
# from typing import List
# class Solution:
#     def closestPrimes(self, left: int, right: int) -> List[int]:
#         def isprime(n: int) -> bool:
#             if n <= 1: return False
#             if n <= 3: return True
#             if n % 2 == 0 or n % 3 == 0: return False
#             limit = int(math.sqrt(n))
#             i = 5
#             while i <= limit:
#                 if n % i == 0 or n % (i + 2) == 0: return False
#                 i += 6
#             return True
        
#         res=float('inf')
#         primes=[-1, -1]
#         i=left
#         while(not isprime(i)): i+=1
#         lastPrime=i
#         for j in range(i+1, right+1):
#             if(isprime(j)): 
#                 if(j-lastPrime<res):
#                     res=min(res, j-lastPrime)
#                     primes=[lastPrime, j]
#                 lastPrime=j
#         return primes

import math
from typing import List
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes
        def get_primes(limit: int) -> List[int]:
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for n in range(2, int(math.sqrt(limit)) + 1):
                if is_prime[n]:
                    for m in range(n * n, limit + 1, n):
                        is_prime[m] = False
            return [i for i in range(left, right + 1) if is_prime[i]]
        
        primes = get_primes(right)
        if len(primes) < 2: return [-1, -1]
        res = [-1, -1]
        min_diff = float('inf')
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                res = [primes[i - 1], primes[i]]
                if min_diff == 2: break
        return res
# 8
# AAAAAAAA - paste
# AAAA - paste+copy
# AA - paste+copy
# A - copy
# 1st copy + last paste + in-between copy-pastes = 1+1+4=6

# 7
# AAAAAAA

# import math
# class Solution:
#     def minSteps(self, n: int) -> int:
#         def log(n): return math.log2(n)
#         if n<2: return 0
#         if n%2!=0: return n
#         return 2+2*(int(log(n))-1)
    
class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        d = 2
        while n > 1:
            while n % d == 0:
                res += d
                n //= d
            d += 1
        return res
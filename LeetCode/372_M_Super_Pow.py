from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def modExp(base, exp, mod):
            res = 1
            base %= mod
            while exp > 0:
                if exp % 2: res = (res * base) % mod
                base = (base * base) % mod
                exp //= 2
            return res

        MOD = 1337
        exp = 0
        for digit in b:
            exp = (exp * 10 + digit) % 1140
        if exp == 0: exp = 1140
        return modExp(a, exp, MOD)
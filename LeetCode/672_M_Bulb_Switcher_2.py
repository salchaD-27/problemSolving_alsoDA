from itertools import product
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0: return 1
        n = min(n, 6)
        seen = set()
        for b1, b2, b3, b4 in product([0, 1], repeat=4):
            total = b1 + b2 + b3 + b4
            if total > presses or (total % 2 != presses % 2): continue
            bulbs = [1] * n
            for i in range(n):
                if b1: bulbs[i] ^= 1
                if b2 and (i + 1) % 2 == 0: bulbs[i] ^= 1
                if b3 and (i + 1) % 2 == 1: bulbs[i] ^= 1
                if b4 and (i + 1) % 3 == 1: bulbs[i] ^= 1
            seen.add(tuple(bulbs))
        return len(seen)
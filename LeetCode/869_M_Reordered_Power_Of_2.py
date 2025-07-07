from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count_n = Counter(str(n))
        for i in range(31):
            power_of_two = 1 << i  # 2^i
            if Counter(str(power_of_two)) == count_n: return True
        return False

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = ''.join(sorted(str(n)))
        for i in range(31):
            power = 1<<i
            if ''.join(sorted(str(power))) == s: return True
        return False
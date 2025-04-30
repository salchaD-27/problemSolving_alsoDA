import random
import bisect
class Solution:
    def __init__(self, w):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total = total
    def pickIndex(self):
        r = random.randint(1, self.total)
        # smallest index such that prefix_sum[i] >= r
        return bisect.bisect_left(self.prefix_sums, r)
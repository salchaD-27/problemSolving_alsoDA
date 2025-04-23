# class Solution:
#     def countLargestGroup(self, n: int) -> int:
#         return sum(int(d) for d in str(n))
    
from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            groups[digit_sum] += 1
        max_size = max(groups.values())
        return sum(1 for size in groups.values() if size == max_size)
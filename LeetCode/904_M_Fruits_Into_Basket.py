# from typing import List
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         if len(fruits)<2: return len(fruits)
#         lastSeen=[fruits[0], fruits[1]]
#         maxTrees=2
#         lastUpdatedIndx=0
#         for i in range(2, len(fruits)):
#             if fruits[i] not in lastSeen:
#                 lastSeen.pop(0)
#                 lastSeen.append(fruits[i])
#                 lastUpdatedIndx=i
#             maxTrees=max(maxTrees,i-lastUpdatedIndx+1)
#         return maxTrees

from typing import List
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0: del count[fruits[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
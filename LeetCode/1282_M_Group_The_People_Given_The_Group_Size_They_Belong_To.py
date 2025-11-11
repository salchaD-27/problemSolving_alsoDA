from typing import List
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        group_mapping = defaultdict(list)
        for i, size in enumerate(groupSizes):
            group_mapping[size].append(i)
            if len(group_mapping[size]) == size: result.append(group_mapping.pop(size))
        return result
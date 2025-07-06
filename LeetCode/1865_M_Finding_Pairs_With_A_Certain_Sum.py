# from typing import List
# class FindSumPairs:
#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1=nums1
#         self.nums2=nums2
#     def add(self, index: int, val: int) -> None: self.nums2[index]+=val
#     def count(self, tot: int) -> int:
#         sortedNums2=sorted(self.nums2)
#         def binarySearch(target):
#             low = 0
#             high = len(sortedNums2) - 1
#             while low <= high:
#                 mid = (low + high) // 2
#                 if sortedNums2[mid] == target: return True
#                 elif sortedNums2[mid] < target: low = mid + 1
#                 else: high = mid - 1
#             return False
#         count=0
#         for i in range(len(self.nums1)):
#             if binarySearch(tot-self.nums1[i]): count+=1
#         return count

from typing import List
from collections import Counter
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)
    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0: del self.counter2[old_val]
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.counter2[new_val] += 1
    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1:
            complement = tot - num
            count += self.counter2.get(complement, 0)
        return count
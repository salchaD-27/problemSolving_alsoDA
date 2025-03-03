import random
from typing import List
class Solution:
    def __init__(self, nums: List[int]):
        self.orig=[]
        self.arr=[]
        for i in range(len(nums)):
            self.orig.append(nums[i])
            self.arr.append(nums[i])
    def reset(self) -> List[int]:
        return self.orig
    def shuffle(self) -> List[int]:
        random.shuffle(self.arr)
        return self.arr
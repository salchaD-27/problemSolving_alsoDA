import random
from typing import List
class Solution:
    def __init__(self, nums: List[int]):
        self.indexMap={}
        for index,value in enumerate(nums):
            if(value in self.indexMap): self.indexMap[value]+=[index]
            else: self.indexMap[value]=[index]
    def pick(self, target: int) -> int:
        return random.choice(self.indexMap[target])
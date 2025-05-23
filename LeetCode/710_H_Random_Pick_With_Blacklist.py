# import random
# from typing import List
# class Solution:
#     def __init__(self, n: int, blacklist: List[int]):
#         blacklist_set = set(blacklist)
#         self.valid_numbers = [i for i in range(n) if i not in blacklist_set]
#     def pick(self) -> int:
#         return random.choice(self.valid_numbers)

import random
from typing import List
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.bound = n - len(blacklist)
        blacklist_set = set(blacklist)
        self.mapping = {}
        last = n - 1
        for b in blacklist:
            if b < self.bound:
                while last in blacklist_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1
    def pick(self) -> int:
        x = random.randint(0, self.bound - 1)
        return self.mapping.get(x, x)
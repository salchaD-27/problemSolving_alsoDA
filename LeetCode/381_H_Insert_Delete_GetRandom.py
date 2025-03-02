import random
from collections import defaultdict
class RandomizedCollection:
    def __init__(self):
        self.arr = []
        self.map = defaultdict(set)
    def insert(self, val: int) -> bool:
        self.map[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.map[val]) == 1 
    def remove(self, val: int) -> bool:
        if not self.map[val]: return False
        remove_index = self.map[val].pop()
        last_element = self.arr[-1] 
        if remove_index != len(self.arr) - 1:
            self.arr[remove_index] = last_element
            self.map[last_element].add(remove_index)
            self.map[last_element].discard(len(self.arr) - 1)
        self.arr.pop()
        if not self.map[val]: del self.map[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)
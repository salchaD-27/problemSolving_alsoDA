# import random
# class RandomizedSet:
#     def __init__(self):
#         self.arr=[]
#     def insert(self, val: int) -> bool:
#         if(val not in self.arr):
#             self.arr.append(val)
#             return True
#         return False
#     def remove(self, val: int) -> bool:
#         if(val in self.arr):
#             self.arr.remove(val)
#             return True
#         return False
#     def getRandom(self) -> int:
#         return random.choice(self.arr)

import random
class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.map = {}
    def insert(self, val: int) -> bool:
        if val in self.map: return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        last_element = self.arr[-1]
        index = self.map[val]
        self.arr[index] = last_element
        self.map[last_element] = index
        self.arr.pop() 
        del self.map[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)
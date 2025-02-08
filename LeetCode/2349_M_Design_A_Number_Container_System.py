# class NumberContainers:
#     def __init__(self):
#         self.container = {}
#     def change(self, index: int, number: int) -> None:
#         self.container[index] = number
#     def find(self, number: int) -> int:
#         indices = [idx for idx, val in self.container.items() if val == number]
#         return min(indices) if indices else -1
    
# class NumberContainers:
#     def __init__(self):
#         self.container = {}
#     def change(self, index: int, number: int) -> None:
#         for key in list(self.container):  
#             if index in self.container[key]:
#                 self.container[key].remove(index)
#                 if not self.container[key]: del self.container[key]
#         if number not in self.container: self.container[number] = []
#         self.container[number].append(index)
#     def find(self, number: int) -> int:
#         if number in self.container and self.container[number]: return min(self.container[number])
#         return -1

from sortedcontainers import SortedSet
class NumberContainers:
    def __init__(self):
        self.index_map = {} 
        self.num_map = {}  
    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            if old_number in self.num_map:
                self.num_map[old_number].discard(index) 
                if not self.num_map[old_number]: del self.num_map[old_number]
        self.index_map[index] = number
        if number not in self.num_map: self.num_map[number] = SortedSet()
        self.num_map[number].add(index)
    def find(self, number: int) -> int:
        if number in self.num_map and self.num_map[number]: return self.num_map[number][0] 
        return -1
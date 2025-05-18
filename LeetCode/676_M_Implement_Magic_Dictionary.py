# from typing import List
# class MagicDictionary:
#     def __init__(self): self.mdic=[]
#     def buildDict(self, dictionary: List[str]) -> None: self.mdic=dictionary
#     def search(self, searchWord: str) -> bool:
#         def is_magic(word: str): return sum(a!=b for a,b in zip(word,searchWord)) == 1
#         return any(is_magic(word) for word in self.mdic)

from typing import List
class MagicDictionary:
    def __init__(self): self.mdic = []
    def buildDict(self, dictionary: List[str]) -> None: self.mdic = dictionary
    def search(self, searchWord: str) -> bool:
        def is_magic(word: str) -> bool:
            if len(word) != len(searchWord): return False
            diff_count = sum(a != b for a, b in zip(word, searchWord))
            return diff_count == 1
        return any(is_magic(word) for word in self.mdic)
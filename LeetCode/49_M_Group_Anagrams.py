from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for str in strs:
            sortedStr = tuple(sorted(str))
            if sortedStr in anagramDict: anagramDict[sortedStr].append(str)
            else: anagramDict[sortedStr] = [str]
        return list(anagramDict.values())
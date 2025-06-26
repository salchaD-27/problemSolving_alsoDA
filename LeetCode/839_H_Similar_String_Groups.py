# from typing import List
# from collections import Counter
# from itertools import permutations
# class Solution:
#     def numSimilarGroups(self, strs: List[str]) -> int:
#         def getAll2AwayStrs(word):
#             res=set()
#             for i in range(len(word)-1):
#                 for j in range(i+1, len(word)):
#                     tempWord = list(word)
#                     tempWord[i], tempWord[j] = tempWord[j], tempWord[i]
#                     res.add(''.join(tempWord))
#             return res

#         chars=Counter(strs[0])
#         allStrs=[''.join(perm) for perm in permutations(chars, len(chars))]
#         groups=[]
#         while allStrs:
#             word=allStrs[0]
#             all2AwayStrs=getAll2AwayStrs(word)
#             for w in all2AwayStrs:
#                 if w in allStrs: allStrs.remove(w)
#             groups.append(all2AwayStrs)
#         groupNums=set()
#         for i in range(len(groups)):
#             for j in range(len(groups[i])):
#                 if groups[i][j] in strs: groupNums.add(i)
#         return len(groupNums)

from typing import List
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1, s2):
            if s1 == s2: return True
            diffs = [(a, b) for a, b in zip(s1, s2) if a != b]
            return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
        visited = set()
        def dfs(i):
            for j in range(len(strs)):
                if j not in visited and isSimilar(strs[i], strs[j]):
                    visited.add(j)
                    dfs(j)
        
        groups = 0
        for i in range(len(strs)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                groups += 1
        return groups
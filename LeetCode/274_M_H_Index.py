# from typing import List
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         def greater(list, val):
#             count=0
#             for num in list:
#                 if num>=val: count+=1
#             return count
        
#         if(len(citations)==1): 
#             if(citations[0]==0): return 0
#             else: return 1
#         citations.sort(reverse=True)
#         for i in range(len(citations)):
#             tempHCriteria=citations[i]
#             tempHCitatations=greater(citations, tempHCriteria)
#             if(tempHCitatations>=tempHCriteria): return tempHCriteria

from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1: h_index = i + 1
            else: break
        return h_index
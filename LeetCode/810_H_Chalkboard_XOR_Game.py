# from typing import List
# class Solution:
#     def xorGame(self, nums: List[int]) -> bool:
#         def allXor(vals): return [vals[i]^vals[i+1] for i in range(len(vals)-1)]
#         def fs(remNums, currTurn):
#             if len(remNums)==2 and currTurn=='A': return False
#             if len(remNums)==2 and currTurn=='B': return True
#             if allXor(remNums)==0: return False
#             if currTurn=='A':
#                 for i in range(len(remNums)):
#                     tempNums=remNums
#                     tempNums.pop(i)
#                     fs(tempNums, 'B')
#             if currTurn=='B':
#                 for i in range(len(remNums)):
#                     tempNums=remNums
#                     tempNums.pop(i)
#                     fs(tempNums, 'A')

#         return fs(nums, 'A')
    
from typing import List
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        total_xor = 0
        for num in nums:
            total_xor ^= num
        return total_xor == 0 or len(nums) % 2 == 0
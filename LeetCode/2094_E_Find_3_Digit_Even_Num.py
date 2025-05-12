# from typing import List
# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         res=[]
#         digits.sort()
        
#         def formulate(currNum, hundredthAdded, tensAdded, lastPlaceAdded):
#             if(lastPlaceAdded<2):
#                 for i in range(len(digits)):
#                     if i!=hundredthAdded and i!=tensAdded: formulate(currNum+digits[i]*10, hundredthAdded, i, 2)
#             else:
#                 for i in range(len(digits)):
#                     if i!=hundredthAdded and i!=tensAdded:
#                         num=currNum+digits[i]
#                         if num%2==0: res.append(currNum)

#         for i in range(len(digits)):
#             if digits[i]!=0: formulate(digits[i]*100, i, -1,  1)
#         return res

from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        def formulate(currNum, hundredthAdded, tensAdded, lastPlaceAdded):
            if lastPlaceAdded < 2:
                for i in range(len(digits)):
                    if i != hundredthAdded and i != tensAdded: formulate(currNum + digits[i]*10, hundredthAdded, i, 2)
            else:
                for i in range(len(digits)):
                    if i != hundredthAdded and i != tensAdded:
                        num = currNum + digits[i]
                        if num % 2 == 0: res.add(num)

        for i in range(len(digits)):
            if digits[i] != 0: formulate(digits[i]*100, i, -1, 1)
        return sorted(res)
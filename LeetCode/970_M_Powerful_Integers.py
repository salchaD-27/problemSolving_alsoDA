# from typing import List
# class Solution:
#     def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
#         ans=2
#         res,powerOfX,powerOfY=[ans],0,1
#         while ans<=bound:
#             ans=x**powerOfX+y**powerOfY
#             res.append(ans)
#             if powerOfX<powerOfY: powerOfX+=1
#             else: powerOfY+=1
#         return res

from typing import List
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
       res , i , j = set() , 0 , 0
       tempx , tempy= x**i , y**j
       while tempx<bound:
           while tempx + tempy <= bound:
               #print("i:{} j:{} x**i:{} y**j:{} add:{}".format(i,j,tempx,tempy,tempx+tempy))
               res.add(tempx+tempy)
               j+=1
               tempy = y**j
               if y==1:  break
           i+=1
           tempx = x**i
           j = 0
           tempy = y**j
           if x==1: break
       return list(res)
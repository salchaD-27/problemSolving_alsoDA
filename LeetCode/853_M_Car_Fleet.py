# # position = [10,8,0,5,3]
# #    speed = [2,4,1,1,3]
# # position = [0,3,5,8,10]
# #    speed = [1,3,1,4,2]
# from typing import List
# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         snt=[[speed[i],position[i]] for i in range(len(position))]
#         snt.sort(lambda x: x[1])
#         fleets=1
#         for i in range(1, len(snt)):
#             if snt[i-1][0]<snt[i][0]: fleets+=1
#         return fleets

from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]: stack.append(time)
        return len(stack)
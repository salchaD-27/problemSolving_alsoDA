# from typing import List
# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         def allNeg(arr):
#             for num in arr:
#                 if num>=0: return False
#             return True
#         def allPos(arr):
#             for num in arr:
#                 if num<0: return False
#             return True

#         while (asteroids and not allNeg(asteroids) and not allPos(asteroids)):
#             for i in range(len(asteroids)-1):
#                 if (asteroids[i]>=0 and asteroids[i+1]>=0) or (asteroids[i]<0 and asteroids[i+1]<0): continue
#                 elif abs(asteroids[i])<abs(asteroids[i+1]): asteroids.pop(i)
#                 elif abs(asteroids[i])>abs(asteroids[i+1]): asteroids.pop(i+1)
#                 elif abs(asteroids[i])==abs(asteroids[i+1]): 
#                     asteroids.pop(i+1)
#                     asteroids.pop(i)
#         return asteroids

# from typing import List
# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack = []
#         for asteroid in asteroids:
#             while stack and asteroid < 0 < stack[-1]:
#                 if stack[-1] < -asteroid: stack.pop()
#                 elif stack[-1] == -asteroid:
#                     stack.pop()
#                     break
#                 else: break
#             else: stack.append(asteroid)
#         return stack

from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if(n > 0): stack.append(n)
            else:
                while(True):
                    if(len(stack) == 0):
                        stack.append(n)
                        break
                    elif(stack[-1] > 0 and stack[-1] > abs(n)): break
                    elif(stack[-1] > 0 and stack[-1] == abs(n)):
                        stack.pop()
                        break
                    elif(stack[-1] > 0 and stack[-1] < abs(n)): stack.pop()
                    else:
                        stack.append(n)
                        break
        return stack
from typing import List
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper(nums):
            if len(nums) == 1: return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j: continue
                    a, b = nums[i], nums[j]
                    nextNums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    for op in ['+', '-', '*', '/']:
                        if op == '+': nextNums.append(a + b)
                        elif op == '-': nextNums.append(a - b)
                        elif op == '*': nextNums.append(a * b)
                        elif op == '/' and b != 0: nextNums.append(a / b)
                        else: continue
                        if helper(nextNums): return True
                        nextNums.pop()
            return False
        return helper(cards)
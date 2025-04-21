# class Solution:
#     def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
#         if(desiredTotal<=maxChoosableInteger): return True
#         currentChance=0
#         while(desiredTotal>maxChoosableInteger and maxChoosableInteger>0):
#             desiredTotal-=maxChoosableInteger
#             maxChoosableInteger-=1
#             currentChance=(currentChance+1)%2
#         return currentChance==0

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0: return True
        if(desiredTotal<=maxChoosableInteger): return True
        total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if total_sum < desiredTotal: return False

        memo = {}
        def can_win(used, total):
            if used in memo: return memo[used]
            for i in range(1, maxChoosableInteger + 1):
                mask = 1 << i
                if not used & mask:
                    if i >= total or not can_win(used | mask, total - i):
                        memo[used] = True
                        return True
            memo[used] = False
            return False
        return can_win(0, desiredTotal)
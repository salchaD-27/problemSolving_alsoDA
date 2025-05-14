# from typing import List
# class Solution:
#     def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
#         cost=0
#         for i in range(len(needs)):
#             cost+=needs[i]*price[i]
#         for i in range(len(special)):
#             tempCost=special[i][-1]
#             for j in range(len(special[i])-1):
#                 if(needs[j]-special[i][j]>0): tempCost+=(needs[j]-special[i][j])*price[i]
#             cost=min(cost, tempCost)
#         return cost

from typing import List
from functools import lru_cache
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @lru_cache(None)
        def dfs(current_needs):
            total = sum(current_needs[i] * price[i] for i in range(len(price)))
            for offer in special:
                new_needs = []
                for i in range(len(price)):
                    if offer[i] > current_needs[i]: break
                    new_needs.append(current_needs[i] - offer[i])
                else: total = min(total, dfs(tuple(new_needs)) + offer[-1])
            return total
        return dfs(tuple(needs))
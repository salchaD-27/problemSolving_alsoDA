from itertools import combinations
class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        n = sum(nums)                                
        nDiv3 = n%3
        if nDiv3 == 0: return n
        terms = [0]+ sorted(filter(lambda x:x%3 != 0, nums))[:4]
        return n - min(map(sum,filter(lambda x: (x[0]+x[1])%3 == nDiv3, combinations(terms,2))))
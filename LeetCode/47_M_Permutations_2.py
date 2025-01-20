from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def generate_permutations(current, remaining):
            if not remaining: return [current]
            permutations = []
            for i in range(len(remaining)):
                num = remaining[i]
                new_remaining = remaining[:i] + remaining[i+1:]
                temp=generate_permutations(current + [num], new_remaining)
                if(temp not in permutations): permutations.extend(temp)
                else: continue
            return permutations
        def pattern(n):
            numbers = list(range(1, n + 1))
            return generate_permutations([], numbers)
        patterns=pattern(len(nums))
        ans=[]
        for pat in patterns:
            temp=[nums[num-1] for num in pat]
            if(temp not in ans): ans.append(temp)
            else: continue
        return ans
from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        def prod(val, nums):
            res = []
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] * nums[j] == val: res.append([nums[i], nums[j]])
            return res

        ans = 0
        seen_products = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp_product = nums[i] * nums[j]
                if temp_product in seen_products:
                    ans += seen_products[temp_product] * 8
                    seen_products[temp_product] += 1
                else: seen_products[temp_product] = 1
        return ans
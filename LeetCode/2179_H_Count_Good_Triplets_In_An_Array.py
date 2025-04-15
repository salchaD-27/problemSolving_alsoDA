from typing import List
class FenwickTree:
    def __init__(self, size): self.tree = [0] * (size + 2)
    def update(self, index, value):
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index
    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res
    
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos_in_nums2 = {val: idx for idx, val in enumerate(nums2)}
        mapped = [pos_in_nums2[val] for val in nums1]
        left_tree = FenwickTree(n)
        left_smaller = [0] * n
        for i in range(n):
            left_smaller[i] = left_tree.query(mapped[i] - 1)
            left_tree.update(mapped[i], 1)
        right_tree = FenwickTree(n)
        right_greater = [0] * n
        for i in range(n - 1, -1, -1):
            right_greater[i] = right_tree.query(n - 1) - right_tree.query(mapped[i])
            right_tree.update(mapped[i], 1)
        total = sum(left_smaller[i] * right_greater[i] for i in range(n))
        return total
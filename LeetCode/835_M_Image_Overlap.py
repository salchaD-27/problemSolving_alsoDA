from typing import List
from collections import Counter
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones_img1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones_img2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        translation_count = Counter()
        for i1, j1 in ones_img1:
            for i2, j2 in ones_img2:
                vector = (i2 - i1, j2 - j1)
                translation_count[vector] += 1
        return max(translation_count.values(), default=0)
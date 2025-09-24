import heapq
from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes):
        freq = Counter(barcodes)
        # Max heap (negative frequency)
        pq = [(-cnt, num) for num, cnt in freq.items()]
        heapq.heapify(pq)
        res = [0] * len(barcodes)
        i = 0

        while pq:
            cnt, num = heapq.heappop(pq)
            for _ in range(-cnt):
                if i >= len(barcodes): i = 1
                res[i] = num
                i += 2
        return res
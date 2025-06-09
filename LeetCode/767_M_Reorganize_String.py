# import heapq
# from collections import Counter
# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         count = Counter(s)
#         maxFreq = max(count.values())
#         remChars = len(s) - maxFreq
#         if remChars < maxFreq - 1: return ''
#         # max heap
#         max_heap = [(-freq, char) for char, freq in count.items()]
#         heapq.heapify(max_heap)
#         result = []
#         while len(max_heap) >= 2:
#             freq1, char1 = heapq.heappop(max_heap)
#             freq2, char2 = heapq.heappop(max_heap)
#             result.extend([char1, char2])
#             if freq1 + 1 < 0: heapq.heappush(max_heap, (freq1 + 1, char1))
#             if freq2 + 1 < 0: heapq.heappush(max_heap, (freq2 + 1, char2))
#         if max_heap:
#             freq, char = heapq.heappop(max_heap)
#             if freq == -1: result.append(char)
#             else: return ''
#         return ''.join(result)

from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_c = 0
        c = ''
        for letter, count in counts.items():
            if count > max_c:
                max_c = count
                c = letter
        if max_c > (len(s)+1)/2: return ""
        res = [''] * len(s)
        i = 0
        while counts[c] > 0:
            res[i] = c
            i+=2
            counts[c]-=1
        for letter, count in counts.items():
            while count > 0:
                if i >= len(s): i = res.index('')
                res[i] = letter
                count -= 1
                i+=2
        return ''.join(res)
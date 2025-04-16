# from typing import List
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         freq = {}
#         for char in chars:
#             if char not in freq: freq[char] = 1
#             else: freq[char] += 1
#         res = []
#         for k, v in freq.items():
#             res.append(k)
#             if v > 1:
#                 for digit in str(v):
#                     res.append(digit)
#         chars[:len(res)] = res
#         return len(res)


from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0
        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write
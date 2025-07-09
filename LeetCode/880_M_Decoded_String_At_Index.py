# class Solution:
#     def decodeAtIndex(self, s: str, k: int) -> str:
#         formedStr,i='',0
#         while(len(formedStr)<k):
#             if s[i] in '0123456789': formedStr+=formedStr*(int(s[i])-1)
#             else: formedStr+=s[i]
#             i+=1
#         return formedStr[k-1]

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch.isdigit(): size *= int(ch)
            else: size += 1
        # backwards
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            k %= size
            if k == 0 and ch.isalpha(): return ch
            if ch.isdigit(): size //= int(ch)
            else: size -= 1
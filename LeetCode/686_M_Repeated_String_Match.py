# class Solution:
#     def repeatedStringMatch(self, a: str, b: str) -> int:
#         for i in range(len(b)):
#             if b[i] not in a: return -1
#         if b in '': return 0
#         checkA,count=a,1
#         while len(a)<3*len(b):
#             if b in checkA: return count
#             count+=1
#             checkA+=a
#         return -1
    
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if set(b) - set(a): return -1
        repeated = a
        count = 1
        while len(repeated) < len(b):
            repeated += a
            count += 1
        if b in repeated: return count
        repeated += a
        if b in repeated: return count + 1
        return -1
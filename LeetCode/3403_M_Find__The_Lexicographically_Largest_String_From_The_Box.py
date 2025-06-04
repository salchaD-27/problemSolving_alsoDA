# from itertools import product
# class Solution:
#     def answerString(self, word: str, numFriends: int) -> str:
#         total=len(word)
#         lens=[i for i in range(1, total)]
#         prods=list(product(lens, repeat=numFriends))
#         res=''
#         for i in range(len(prods)):
#             if sum(prods[i])==total:
#                 subStr=word[:prods[i][0]]
#                 subLen=len(subStr)
#                 for j in range(1, len(prods[i])):
#                     startIdx=sum(prods[i][:j])
#                     tempStr=word[startIdx:startIdx+prods[i][j]]
#                     if len(tempStr)>=subLen and tempStr>subStr: 
#                         subStr=tempStr
#                         subLen=len(tempStr)
#                 if subStr>res: res=subStr
#         return res

# from itertools import product
# class Solution:
#     def answerString(self, word: str, numFriends: int) -> str:
#         total = len(word)
#         if numFriends == 1: return word
#         lens = [i for i in range(1, total + 1)]
#         prods = list(product(lens, repeat=numFriends))
#         res = ''
#         for p in prods:
#             if sum(p) == total:
#                 maxSub = ''
#                 idx = 0
#                 for length in p:
#                     sub = word[idx:idx + length]
#                     if sub > maxSub: maxSub = sub
#                     idx += length
#                 if maxSub > res: res = maxSub
#         return res

# class Solution:
#     def answerString(self, word: str, numFriends: int) -> str:
#         self.res = ""
#         n = len(word)
#         def backtrack(index: int, cutsLeft: int, maxSub: str):
#             if cutsLeft == 1:
#                 part = word[index:]
#                 maxSub = max(maxSub, part)
#                 self.res = max(self.res, maxSub)
#                 return
#             for i in range(index + 1, n - cutsLeft + 2):
#                 part = word[index:i]
#                 backtrack(i, cutsLeft - 1, max(maxSub, part))
#         backtrack(0, numFriends, "")
#         return self.res

class Solution(object):
    def answerString(self, word, numFriends):
        if numFriends == 1: return word
        res = ""
        length = len(word) - numFriends + 1
        for i in range(0, len(word)):
            temp = word[i : i + length]
            if temp > res: res = temp
        return res
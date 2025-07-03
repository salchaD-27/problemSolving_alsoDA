import string
class Solution:
    def kthCharacter(self, k: int) -> str:
        nextChar = {}
        letters = string.ascii_lowercase  #'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(letters)):
            nextChar[letters[i]] = letters[(i + 1) % 26]
        res='a'
        while len(res)<k:
            tempRes=[nextChar[i] for i in res]
            res+=''.join(tempRes)
        return res[k-1]
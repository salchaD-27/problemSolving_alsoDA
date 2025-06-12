class Solution:
    def customSortString(self, order: str, s: str) -> str:
        commonCharFreq={}
        leftOverStr=''
        for i in range(len(s)):
            if s[i] in order:
                if s[i] in commonCharFreq: commonCharFreq[s[i]]+=1
                else: commonCharFreq[s[i]]=1
            else: leftOverStr+=s[i]
        sortedStr=''
        for i in range(len(order)):
            if order[i] in commonCharFreq: sortedStr+=order[i]*commonCharFreq[order[i]]
        return sortedStr+leftOverStr
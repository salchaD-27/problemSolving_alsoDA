class Solution:
    def maskPII(self, s: str) -> str:
        def justStr(s):
            newS=''
            for i in range(len(s)):
                if s[i] not in '-+() ': newS+=s[i]
            return newS
        def maskEmail(s):
            s=s.lower()
            s=s.split('@')
            return s[0][0]+'*****'+s[0][-1]+'@'+s[1]
        def maskPhone(s):
            n=len(s)
            if n==10: return '***-***-'+s[-4:]
            elif n==11: return '+*-***-***-'+s[-4:]
            elif n==12: return '+**-***-***-'+s[-4:]
            else: return '+***-***-***-'+s[-4:]
        
        if '@' in s: return maskEmail(s)
        return maskPhone(justStr(s))
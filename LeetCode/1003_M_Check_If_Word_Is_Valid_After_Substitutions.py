class Solution:
    def isValid(self, s: str) -> bool:
        if s == "abc" : return True
        if s[0] != "a" or s[-1] != "c" : return False
        l = list(s)
        for j in range(len(l)) :
            for i in range(0,len(l)-2) :
                if l == ["a","b","c"] : return True
                if i + 2 <= len(l) - 1 :
                    if l[i] + l[i+1] + l[i+2] == "abc" :
                        for x in range(3) :
                            l.pop(i)
        if len(l) == 0 : return True
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "c":
                if len(stack) < 2 or stack[-2] != "a" or stack[-1] != "b": return False
                stack.pop()
                stack.pop()
            else: stack.append(c)
        return len(stack) == 0
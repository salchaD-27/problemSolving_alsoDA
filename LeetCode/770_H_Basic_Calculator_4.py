# from typing import List
# class Solution:
#     def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
#         valOf={}
#         for i in range(len(evalvars)):
#             valOf[evalvars[i]]=evalints[i]
#         simpleExp=''
#         for exp in expression.split(' '):
#             if '(' in exp:
#                 simpleExp+='('
#                 if exp[1:] in evalvars: simpleExp+=str(valOf[exp[1:]])
#                 else: simpleExp+=exp[1:]
#             elif ')' in exp:
#                 if exp[:-1] in evalvars: simpleExp+=str(valOf[exp[:-1]])
#                 else: simpleExp+=exp[:-1]
#                 simpleExp+=')'
#             elif exp in evalvars: simpleExp+=str(valOf[exp])
#             else: simpleExp+=exp
#             simpleExp+=' '

#         tokens = simpleExp.strip().split()
#         expMap = {'const': 0}
#         lastSign = 1
#         for tok in tokens:
#             if tok == '+': lastSign = 1
#             elif tok == '-': lastSign = -1
#             else:
#                 try:
#                     num = int(tok)
#                     expMap['const'] += lastSign * num
#                 except:
#                     if tok in expMap: expMap[tok] += lastSign
#                     else: expMap[tok] = lastSign
#         output = []
#         for key in sorted(expMap.keys()):
#             coeff = expMap[key]
#             if coeff == 0: continue
#             if key == 'const': output.append(str(coeff))
#             else:
#                 if coeff == 1: output.append(key)
#                 else: output.append(f"{coeff}*{key}")
#         return output

# from typing import List
# class Solution:
#     def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
#         valOf = dict(zip(evalvars, evalints))
#         simpleExp = ''
#         for exp in expression.split(' '):
#             if '(' in exp:
#                 simpleExp += '('
#                 inner = exp[1:]
#                 simpleExp += str(valOf.get(inner, inner))
#             elif ')' in exp:
#                 inner = exp[:-1]
#                 simpleExp += str(valOf.get(inner, inner))
#                 simpleExp += ')'
#             elif exp in valOf: simpleExp += str(valOf[exp])
#             else: simpleExp += exp
#             simpleExp += ' '
#         tokens = simpleExp.strip().split()
#         expMap = {}
#         lastSign = 1
#         for tok in tokens:
#             if tok == '+': lastSign = 1
#             elif tok == '-': lastSign = -1
#             else:
#                 try:
#                     num = int(tok)
#                     expMap['const'] = expMap.get('const', 0) + lastSign * num
#                 except: expMap[tok] = expMap.get(tok, 0) + lastSign
#         def sort_key(term):
#             if term == 'const': return (1, '')
#             return (0, term)
#         sorted_terms = sorted(expMap.items(), key=lambda x: sort_key(x[0]))
#         result = []
#         for var, coeff in sorted_terms:
#             if coeff == 0: continue
#             if var == 'const': result.append(str(coeff))
#             else:
#                 if coeff == 1: result.append(f"{var}")
#                 elif coeff == -1: result.append(f"-1*{var}")
#                 else: result.append(f"{coeff}*{var}")
#         return result

import re
from collections import Counter
def basicCalculatorIV(self, expression, evalvars, evalints):
    class C(Counter):
        def __add__(self, other):
            self.update(other)
            return self
        def __sub__(self, other):
            self.subtract(other)
            return self
        def __mul__(self, other):
            product = C()
            for x in self:
                for y in other:
                    xy = tuple(sorted(x + y))
                    product[xy] += self[x] * other[y]
            return product
    vals = dict(zip(evalvars, evalints))
    def f(s):
        s = str(vals.get(s, s))
        return C({(s,): 1}) if s.isalpha() else C({(): int(s)})
    c = eval(re.sub('(\w+)', r'f("\1")', expression))
    return ['*'.join((str(c[x]),) + x)
            for x in sorted(c, key=lambda x: (-len(x), x))
            if c[x]]
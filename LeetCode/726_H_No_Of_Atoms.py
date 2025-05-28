# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         def add(d1, d2):
#             result = {}
#             keys = set(d1.keys()).union(d2.keys())
#             for key in keys:
#                 result[key] = d1.get(key, 0) + d2.get(key, 0)
#             return result
#         def multiply(d, num): return {key: value * num for key, value in d.items()}
#         def subCount(multiplier, formula):
#             if '(' not in formula and ')' not in formula:
#                 tempdict={}
#                 stack=[]
#                 for i in range(len(formula)):
#                     if(capital(formula[i])): 
#                         if not stack: stack.append(formula[i])
#                         if stack:
#                             element=''
#                             while stack:
#                                 element+=stack[-1]
#                                 stack.pop(-1)
#                             tempdict[element[::-1]]=1
#                     elif num(formula[i]):
#                         element=''
#                         while stack:
#                             element+=stack[-1]
#                             stack.pop(-1)
#                         tempdict[element[::-1]]=int(formula[i])
#                     else: stack.append(formula[i])
#                 return multiply(tempdict, multiplier)
#             else:
#                 openIdx,closeIdx=0,0
#                 for i in range(len(formula)):
#                     if formula[i]=='(': 
#                         openIdx=i
#                         break
#                 for i in reversed(range(len(formula))):
#                     if formula[i]==')': 
#                         closeIdx=i
#                         break
#                 toMultiply=''
#                 for i in range(closeIdx+1, len(formula)):
#                     if(num(formula[i])): toMultiply+=formula[i]
#                     else: break
#                 return add(subCount(1, formula[:openIdx]), subCount(int(toMultiply), formula[openIdx:closeIdx+1]), subCount(1, formula[closeIdx+1:]))
#         return subCount(1, formula)

# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         def add(d1, d2):
#             result = {}
#             keys = set(d1.keys()).union(d2.keys())
#             for key in keys:
#                 result[key] = d1.get(key, 0) + d2.get(key, 0)
#             return result
#         def multiply(d, num): return {key: value * num for key, value in d.items()}
#         def is_capital(c): return 'A' <= c <= 'Z'
#         def is_lower(c): return 'a' <= c <= 'z'
#         def is_digit(c): return '0' <= c <= '9'
#         def subCount(multiplier, formula):
#             if '(' not in formula:
#                 tempdict = {}
#                 i = 0
#                 while i < len(formula):
#                     if is_capital(formula[i]):
#                         element = formula[i]
#                         i += 1
#                         while i < len(formula) and is_lower(formula[i]):
#                             element += formula[i]
#                             i += 1
#                         count_str = ''
#                         while i < len(formula) and is_digit(formula[i]):
#                             count_str += formula[i]
#                             i += 1
#                         count = int(count_str) if count_str else 1
#                         if element in tempdict: tempdict[element] += count
#                         else: tempdict[element] = count
#                 return multiply(tempdict, multiplier)
#             openIdx, closeIdx = -1, -1
#             level = 0
#             for i in range(len(formula)):
#                 if formula[i] == '(':
#                     if level == 0:
#                         openIdx = i
#                     level += 1
#                 elif formula[i] == ')':
#                     level -= 1
#                     if level == 0:
#                         closeIdx = i
#                         break
#             i = closeIdx + 1
#             toMultiply = ''
#             while i < len(formula) and is_digit(formula[i]):
#                 toMultiply += formula[i]
#                 i += 1
#             multiplier_inside = int(toMultiply) if toMultiply else 1
#             before = formula[:openIdx]
#             inside = formula[openIdx + 1:closeIdx]
#             after = formula[i:]
#             return add(add(subCount(1, before), subCount(multiplier_inside, inside)),subCount(1, after))

#         result_dict = subCount(1, formula)
#         return ''.join(f"{atom}{(result_dict[atom] if result_dict[atom] > 1 else '')}" for atom in sorted(result_dict))
    
from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        N = len(formula)
        while i < N:
            if formula[i] == "(":
                stack.append(Counter())
            elif formula[i] == ")":
                num = 0
                while i + 1 < N and formula[i + 1].isdigit():
                    num = num * 10 + int(formula[i + 1])
                    i += 1
                num = 1 if num == 0 else num
                item = stack.pop()
                for index, value in item.items():
                    stack[-1][index] += value * num
            else:
                element = formula[i]
                while i + 1 < N and formula[i + 1].islower():
                    element += formula[i + 1]
                    i += 1
                num = 0
                while i + 1 < N and formula[i + 1].isdigit():
                    num = num * 10 + int(formula[i + 1])
                    i += 1
                num = 1 if num == 0 else num
                stack[-1][element] += num
            i += 1

        result = ""
        for key in sorted(stack[-1].keys()):
            num = str(stack[-1][key]) if stack[-1][key] > 1 else ""
            result += key + num
        return result
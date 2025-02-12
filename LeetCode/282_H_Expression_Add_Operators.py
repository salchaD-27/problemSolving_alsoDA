# from typing import List
# from itertools import product
# # from itertools import combinations_with_replacement as cwr
# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:
#         res=[]
#         ops = ['+', '-', '*']
#         operatorCombs = list(product(ops, repeat=len(num) - 1))
#         for operators in operatorCombs:
#             expression = num[0]
#             for i in range(len(operators)):
#                 expression += operators[i] + num[i + 1]
#             if(eval(expression)==target): res.append(expression)
#         return res

# from typing import List
# from itertools import product
# from itertools import combinations
# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:
#         def generate_variants(arr):
#             results = [arr] 
#             zero_positions = [i for i in range(1, len(arr)) if arr[i] == 0]
#             for size in range(1, len(zero_positions) + 1): 
#                 for merge_indices in combinations(zero_positions, size):
#                     new_arr = arr[:]
#                     for idx in sorted(merge_indices, reverse=True): 
#                         new_arr[idx - 1] = int(str(new_arr[idx - 1]) + '0') 
#                         new_arr.pop(idx) 
#                     results.append(new_arr)
#             return results
        
#         def subSolution(t, target):
#             res=[]
#             ops = ['+', '-', '*']
#             operatorCombs = list(product(ops, repeat=len(num) - 1))
#             for operators in operatorCombs:
#                 expression = num[0]
#                 for i in range(len(operators)):
#                     expression += operators[i] + num[i + 1]
#                 if(eval(expression)==target): res.append(expression)
#             return res
        
#         res=[]
#         nums=[int(char) for char in num]
#         temp=generate_variants(nums)
#         for t in temp:
#             res+=subSolution(t, target)
#         return res

from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(index, expression, prev_operand, current_value):
            if index == len(num):
                if current_value == target: res.append(expression)
                return
            for i in range(index, len(num)):
                sub_str = num[index:i+1]
                sub_value = int(sub_str)
                if sub_str[0] == '0' and len(sub_str) > 1: break

                if index == 0: backtrack(i + 1, sub_str, sub_value, sub_value)
                else:
                    backtrack(i + 1, expression + "+" + sub_str, sub_value, current_value + sub_value)
                    backtrack(i + 1, expression + "-" + sub_str, -sub_value, current_value - sub_value)
                    backtrack(i + 1, expression + "*" + sub_str, prev_operand * sub_value, current_value - prev_operand + (prev_operand * sub_value))
        
        res = []
        backtrack(0, "", 0, 0)
        return res
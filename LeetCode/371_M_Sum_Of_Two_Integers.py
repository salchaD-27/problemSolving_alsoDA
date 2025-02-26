# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         def toBinary(n):
#             if n >= 0: return bin(n)[2:]
#             else:
#                 bits = n.bit_length() + 1 
#                 return bin((1 << bits) + n)[2:]
#         def toDecimal(binary_str):
#             if binary_str[0] == '1':  
#                 bits = len(binary_str)
#                 return int(binary_str, 2) - (1 << bits)
#             else: return int(binary_str, 2)
#         def binaryAdd(a,b):
#             mask = 0xFFFFFFFF
#             while b != 0:
#                 carry = (a & b) << 1 
#                 a = (a ^ b) & mask   
#                 b = carry & mask       
#             if a >> 31 & 1: return bin(a | ~mask)
#             return bin(a)[2:]
#         return toDecimal(binaryAdd(toBinary(a), toBinary(b)))

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         while b != 0:
#             carry = (a & b) << 1
#             a = a ^ b 
#             b = carry 
#         return a
    
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  
        while b != 0:
            carry = (a & b) << 1  
            a = (a ^ b) & mask  
            b = carry & mask  
        if a > 0x7FFFFFFF: return ~(a ^ mask)
        return a
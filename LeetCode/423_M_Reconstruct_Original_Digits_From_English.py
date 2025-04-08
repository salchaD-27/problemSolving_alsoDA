# class Solution:
#     def originalDigits(self, s: str) -> str:
#         origRef=['zero','one','two','three','four','five','six','seven','eight','nine']
#         ref=['zero','one','two','three','four','five','six','seven','eight','nine']
#         ans=[]
#         i=0
#         while(len(s)>0):
#             for j in range(len(ref)):
#                 if(ref[j][0]==s[i]):
#                     if(len(ref[j])==1):
#                         ref[j]=origRef[j]
#                         ans.append(j)
#                         break
#                     ref[j]=ref[j][1:]
#                     break
#             i+=1
#             if i==len(s): i=0
#         res=''
#         ans.sort()
#         for num in ans:
#             res+=str(num)
#         return res

from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        unique_chars = {
            'z': '0',  # 'z' is unique to "zero"
            'w': '2',  # 'w' is unique to "two"
            'u': '4',  # 'u' is unique to "four"
            'x': '6',  # 'x' is unique to "six"
            'g': '8',  # 'g' is unique to "eight"
            'h': '3',  # 'h' is unique to "three" (after '8' is removed)
            'f': '5',  # 'f' is unique to "five" (after '4' is removed)
            's': '7',  # 's' is unique to "seven" (after '6' is removed)
            'o': '1',  # 'o' is unique to "one" (after '0', '2', '4' are removed)
            'i': '9'   # 'i' is unique to "nine" (after '5', '6', '8' are removed)
        }
        digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        count = Counter(s)
        digit_count = [0] * 10
        for char, digit in unique_chars.items():
            digit_count[int(digit)] = count[char]
            for c in digit_words[int(digit)]:
                count[c] -= digit_count[int(digit)]
        result = []
        for i in range(10):
            result.extend([str(i)] * digit_count[i])
        return ''.join(sorted(result))
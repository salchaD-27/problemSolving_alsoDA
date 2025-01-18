# from typing import List
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         def generate_permutations(current, remaining):
#             if not remaining: return [current]
#             permutations = []
#             for i in range(len(remaining)):
#                 num = remaining[i]
#                 new_remaining = remaining[:i] + remaining[i+1:]
#                 permutations.extend(generate_permutations(current + [num], new_remaining))
#             return permutations
#         def pattern(n):
#             numbers = list(range(1, n + 1))
#             return generate_permutations([], numbers)
#         def remove_duplicates(arr):
#             seen = set()
#             result = []
#             for item in arr:
#                 if item not in seen:
#                     result.append(item)
#                     seen.add(item)
#             return result
#         def find_all_occurrences(s: str, pat: str):
#             indices = []
#             start = 0 
#             while True:
#                 index = s.find(pat, start)
#                 if index == -1: break  
#                 indices.append(index) 
#                 start = index + 1  
#             return indices
        
#         numPatterns=pattern(len(words))
#         strPatterns=[]
#         for i in range(len(numPatterns)):
#             temp=''
#             for j in range(len(numPatterns[i])):
#                 temp+=words[numPatterns[i][j]-1]
#             strPatterns.append(temp)
#         strPatterns=remove_duplicates(strPatterns)
#         ans=[]
#         for pat in strPatterns:
#             if(pat in s): 
#                 tempAns=find_all_occurrences(s, pat)
#                 for num in tempAns: ans.append(num)
#         ans.sort()
#         return ans


from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s: return []
        word_len = len(words[0]) 
        word_count = len(words)  
        word_map = {}            
        result = []
        for word in words:
            if word not in word_map:
                word_map[word] = 0
            word_map[word] += 1
        for i in range(word_len):
            left = i
            right = i
            current_map = {}  
            count = 0 
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                if word in word_map:
                    if word not in current_map:
                        current_map[word] = 0
                    current_map[word] += 1
                    count += 1
                    while current_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        current_map[left_word] -= 1
                        left += word_len
                        count -= 1
                    if count == word_count: result.append(left)
                else:
                    current_map.clear()
                    count = 0
                    left = right
        return result
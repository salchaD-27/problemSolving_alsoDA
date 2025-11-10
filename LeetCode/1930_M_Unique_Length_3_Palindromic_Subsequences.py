class Solution:
    def countPalindromicSubsequence(self, inputString):
        min_exist = [float('inf')] * 26
        max_exist = [float('-inf')] * 26
        for i in range(len(inputString)):
            char_index = ord(inputString[i]) - ord('a')
            min_exist[char_index] = min(min_exist[char_index], i)
            max_exist[char_index] = max(max_exist[char_index], i)
        unique_count = 0
        for char_index in range(26):
            if min_exist[char_index] == float('inf') or max_exist[char_index] == float('-inf'): continue
            unique_chars_between = set()
            for j in range(min_exist[char_index] + 1, max_exist[char_index]):
                unique_chars_between.add(inputString[j])
            unique_count += len(unique_chars_between)
        return unique_count
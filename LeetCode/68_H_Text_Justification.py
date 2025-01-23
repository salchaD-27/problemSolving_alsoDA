# from typing import List
# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         result = []
#         line, line_length = [], 0
#         for word in words:
#             if line_length + len(line) + len(word) > maxWidth:
#                 for i in range(maxWidth - line_length):
#                     line[i % (len(line) - 1 or 1)] += ' '
#                 result.append(''.join(line))
#                 line, line_length = [], 0
#             line.append(word)
#             line_length += len(word)
#         result.append(' '.join(line).ljust(maxWidth))
#         return result
    


from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(words, maxWidth, i, j, is_last_line):
            line_words = words[i:j]
            total_word_length = sum(len(word) for word in line_words)
            total_spaces = maxWidth - total_word_length
            if is_last_line or len(line_words) == 1: return ' '.join(line_words).ljust(maxWidth)
            gaps = len(line_words) - 1
            space_per_gap = total_spaces // gaps
            extra_spaces = total_spaces % gaps
            line = ''
            for k in range(len(line_words)):
                line += line_words[k]
                if k < gaps: line += ' ' * (space_per_gap + (1 if k < extra_spaces else 0))
            return line
        
        ans = []
        i = 0
        while i < len(words):
            j = i
            current_length = 0
            while j < len(words) and current_length + len(words[j]) + (j - i) <= maxWidth:
                current_length += len(words[j])
                j += 1
            is_last_line = j == len(words)
            ans.append(justify(words, maxWidth, i, j, is_last_line))
            i = j
        return ans
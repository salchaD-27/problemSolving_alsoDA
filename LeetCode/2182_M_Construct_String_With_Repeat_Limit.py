class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        sorted_chars = sorted(freq.keys(), reverse=True)
        result = []
        while sorted_chars:
            char = sorted_chars[0]
            count = min(freq[char], repeatLimit)
            result.append(char * count)
            freq[char] -= count
            
            if freq[char] > 0:
                if len(sorted_chars) > 1:
                    next_char = sorted_chars[1]
                    result.append(next_char)
                    freq[next_char] -= 1
                    if freq[next_char] == 0:
                        sorted_chars.pop(1)
                else: break
            else: sorted_chars.pop(0)
        return ''.join(result)
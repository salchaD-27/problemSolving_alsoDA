# 3[a]2[bc]
# bc
# bc
# a
# a
# a

# 3[a2[c]]
# accaccacc
# a2[c]
# c
# c
# a
# a2[c]
# a2[c]
# a2[c]

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        curr_num = 0
        for char in s:
            if char.isdigit(): curr_num = curr_num * 10 + int(char)
            elif char == "[":
                stack.append((curr_string, curr_num)) 
                curr_string = ""
                curr_num = 0
            elif char == "]":
                last_string, num = stack.pop()
                curr_string = last_string + num * curr_string 
            else: curr_string += char 
        return curr_string
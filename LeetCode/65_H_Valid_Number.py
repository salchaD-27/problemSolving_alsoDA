# import re
# from typing import List
# class Solution:
#     def isNumber(self, s: str) -> bool:
#         pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
#         return re.match(pattern, s.strip()) is not None


from typing import List
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s: return False
        has_digit = False
        has_dot = False
        has_e = False
        has_sign = False
        for i, char in enumerate(s):
            # Sign at beginning or after e/E
            if char in ['+', '-']:
                if i > 0 and s[i-1] not in ['e', 'E']:  return False
                has_sign = True
            # Exponent
            # Only one e/E allowed, after digits
            elif char in ['e', 'E']:
                if has_e or not has_digit: return False
                has_e = True
                has_digit = False  # Digits after e/E
            # Decimal point
            elif char == '.':
                if has_dot: return False
                # No decimal point after e/E
                if has_e: return False
                has_dot = True
            # Digits
            elif char.isdigit(): has_digit = True
            else: return False
        return has_digit
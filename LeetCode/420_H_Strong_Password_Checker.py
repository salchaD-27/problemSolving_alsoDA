# class Solution:
#     def strongPasswordChecker(self, password: str) -> int:
#         def hasLower(password): return any(c.islower() for c in password)
#         def hasUpper(password): return any(c.isupper() for c in password)
#         def hasDigit(password): return any(c.isdigit() for c in password)
#         def hasTriple(password):
#             for i in range(2, len(password)):
#                 if password[i] == password[i - 1] == password[i - 2]: return True
#             return False

#         n = len(password)
#         changes = 0
#         has_lower = hasLower(password)
#         has_upper = hasUpper(password)
#         has_digit = hasDigit(password)
#         has_triple = hasTriple(password)
#         if not has_lower: changes += 1
#         if not has_upper: changes += 1
#         if not has_digit: changes += 1
#         if has_triple: changes += 1
#         if n < 6: changes = max(changes, 6 - n)
#         elif n > 20: changes = max(changes, n - 20)
#         return changes

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): missing_type -= 1
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1
        change = 0
        one = two = 0
        p = 2
        while p < len(s):
            if s[p] == s[p-1] == s[p-2]:
                length = 2
                while p < len(s) and s[p] == s[p-1]:
                    length += 1
                    p += 1   
                change += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else: p += 1
        if len(s) < 6: return max(missing_type, 6 - len(s))
        elif len(s) <= 20: return max(missing_type, change)
        else:
            delete = len(s) - 20
            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) // 2 
            change -= max(delete - one - 2 * two, 0) // 3  
            return int(delete + max(missing_type, change))
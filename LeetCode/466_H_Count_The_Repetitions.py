# class Solution:
#     def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
#         def derivable(target, source):
#             t_idx, s_idx = 0, 0
#             while t_idx < len(target) and s_idx < len(source):
#                 if target[t_idx] == source[s_idx]: t_idx += 1
#                 s_idx += 1
#             return t_idx == len(target)

#         str1=s1*n1
#         str2=s2*n2
#         i=1
#         while(True):
#             str3=str2*i
#             if(derivable(str3, str1)): i+=1
#             else: break
#         return i-1

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0: return 0
        s1_count = 0
        s2_count = 0
        index = 0
        recall = dict()
        while s1_count < n1:
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2_count += 1
                        index = 0
            s1_count += 1
            if index in recall:
                prev_s1_count, prev_s2_count = recall[index]
                cycle_len = s1_count - prev_s1_count
                cycle_s2s = s2_count - prev_s2_count
                remaining_cycles = (n1 - s1_count) // cycle_len
                s1_count += remaining_cycles * cycle_len
                s2_count += remaining_cycles * cycle_s2s
            else: recall[index] = (s1_count, s2_count)
        return s2_count // n2
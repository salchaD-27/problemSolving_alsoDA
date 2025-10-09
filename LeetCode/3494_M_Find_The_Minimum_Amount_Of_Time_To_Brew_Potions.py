# from typing import List
# class Solution:
#     def minTime(self, skill: List[int], mana: List[int]) -> int:
#         n, m = len(skill), len(mana)
#         done = [0] * (n + 1)
#         for j in range(m):
#             for i in range(n): done[i + 1] = max(done[i + 1], done[i]) + mana[j] * skill[i]
#             for i in range(n - 1, 0, -1): done[i] = done[i + 1] - mana[j] * skill[i]
#         return done[n]

from typing import List
class Solution:
    def minTime(self, skills: List[int], energy: List[int]) -> int:
        n, m = len(skills), len(energy)
        prefix_skills = [0] * n
        for i in range(1, n):
            prefix_skills[i] = prefix_skills[i - 1] + skills[i]
        total_time = skills[0] * energy[0]
        for j in range(1, m):
            max_time = skills[0] * energy[j]
            for i in range(1, n):
                diff_time = prefix_skills[i] * energy[j - 1] - prefix_skills[i - 1] * energy[j]
                if diff_time > max_time: max_time = diff_time
            total_time += max_time
        return total_time + prefix_skills[-1] * energy[-1]
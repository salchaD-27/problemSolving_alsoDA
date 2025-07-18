# from typing import List
# class TopVotedCandidate:
#     def __init__(self, persons: List[int], times: List[int]):
#         self.persons=persons
#         self.times=times
#     def q(self, t: int) -> int:
#         def getLastVoteIdx(time):
#             for i in range(len(self.times)):
#                 if time<self.times[i]: return i
#         idx=getLastVoteIdx(t)
#         votes={}
#         for vote in self.persons[:idx]:
#             if vote in votes: votes[vote]+=1
#             else: votes[vote]=1

import bisect
from typing import List
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        vote_counts = {}
        leader = -1
        max_votes = 0
        for p in persons:
            vote_counts[p] = vote_counts.get(p, 0) + 1
            if vote_counts[p] >= max_votes:
                if p != leader: leader = p
                max_votes = vote_counts[p]
            self.leaders.append(leader)
    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]
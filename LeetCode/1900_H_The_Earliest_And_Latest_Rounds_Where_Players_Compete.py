from functools import lru_cache
from typing import List
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dp(players_tuple):
            players = list(players_tuple)
            round_number = 1
            queue = [(players, 1)]
            earliest, latest = float('inf'), -float('inf')
            while queue:
                next_queue = []
                for curr_players, round_no in queue:
                    length = len(curr_players)
                    matchups = []
                    for i in range(length // 2):
                        a = curr_players[i]
                        b = curr_players[-1 - i]
                        matchups.append((a, b))
                    middle = [curr_players[length // 2]] if length % 2 == 1 else []

                    def backtrack(idx, next_players):
                        nonlocal earliest, latest
                        if idx == len(matchups):
                            next_round = sorted(next_players + middle)
                            next_queue.append((next_round, round_no + 1))
                            return
                        a, b = matchups[idx]
                        if {a, b} == {firstPlayer, secondPlayer}:
                            earliest = min(earliest, round_no)
                            latest = max(latest, round_no)
                            return
                        if a == firstPlayer or a == secondPlayer: backtrack(idx + 1, next_players + [a])
                        elif b == firstPlayer or b == secondPlayer: backtrack(idx + 1, next_players + [b])
                        else:
                            backtrack(idx + 1, next_players + [a])
                            backtrack(idx + 1, next_players + [b])
                    backtrack(0, [])
                queue = next_queue
            return [earliest, latest]
        return dp(tuple(range(1, n + 1)))
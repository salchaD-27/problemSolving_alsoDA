from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(str): return str == str[::-1]
        def backtrack(start: int, path: List[str]):
            if start == len(s):
                ans.append(path[:])
                return
            for end in range(start, len(s)): 
                if is_palindrome(s[start:end+1]): 
                    path.append(s[start:end+1]) 
                    backtrack(end+1, path) 
                    path.pop()  
        
        ans = []
        backtrack(0, [])
        return ans
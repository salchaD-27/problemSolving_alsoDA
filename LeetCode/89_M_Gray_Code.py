from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        smaller_gray_code = self.grayCode(n - 1)
        reflected = [(1 << (n - 1)) | x for x in reversed(smaller_gray_code)]
        return smaller_gray_code + reflected
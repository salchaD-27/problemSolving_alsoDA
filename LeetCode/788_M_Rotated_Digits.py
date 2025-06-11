class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotate_map = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}
        good_count = 0
        for num in range(1, n + 1):
            s = str(num)
            rotated = []
            is_valid = True
            for ch in s:
                if ch not in rotate_map:
                    is_valid = False
                    break
                rotated.append(rotate_map[ch])
            if is_valid and ''.join(rotated) != s: good_count += 1
        return good_count
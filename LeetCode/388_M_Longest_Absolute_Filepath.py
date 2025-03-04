# # dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext
# # dir \tsubdir1 \t\tfile1.ext \t\tsubsubdir1 \tsubdir2 \t\tsubsubdir2 \t\t\tfile2.ext
# 0: dir
# 1: subdir1: dir, subdir2: dir
# 2: file1.ext: subdir1, subsubdir1: subdir1, subsubdir2: subdir2
# 3: file2.ext: subsubdir2

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        max_length = 0
        path_lengths = {0: 0}
        for line in input.split("\n"):
            depth = line.count("\t")
            name = line.lstrip("\t")
            if '.' in name: max_length = max(max_length, path_lengths[depth] + len(name))
            else: path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1
        return max_length
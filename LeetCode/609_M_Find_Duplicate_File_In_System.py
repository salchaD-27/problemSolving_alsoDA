# from typing import List
# class Solution:
#     def findDuplicate(self, paths: List[str]) -> List[List[str]]:
#         fileMap={} # root:[files]
#         for path in paths:
#             files=path.split(' ')
#             root=files[0]
#             content=[]
#             for file in files[1:]:
#                 content.append([file.split('.')[0],file.split('(')[-1][:-1]])
#             fileMap[root]=content
        
from typing import List
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            for file_info in parts[1:]:
                name, content = file_info.split('(')
                content = content[:-1]
                full_path = f"{directory}/{name}"
                content_map[content].append(full_path)
        return [files for files in content_map.values() if len(files) > 1]
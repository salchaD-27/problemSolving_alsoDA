# from typing import List
# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
#         folders=[]
#         for fold in folder:
#             if not folders or fold.startswith(folders[-1]+"/"):
#                 folders.append(fold)
#             else:
#                 while folders and not fold.startswith(folders[-1]+"/"):
#                     folders.pop()
#                     folders.append(fold)
#         return folders

from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + "/"): res.append(path)
        return res
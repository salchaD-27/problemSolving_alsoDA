# from typing import List
# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         sentence=sentence.split(' ')
#         for i in range(len(dictionary)):
#             root=dictionary[i]
#             rootLen=len(root)
#             for j in range(len(sentence)):
#                 if(len(sentence[i])>=rootLen and sentence[:rootLen]==root): sentence[i]=root
#         return ' '.join(sentence)

from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        words = sentence.split()
        for i in range(len(words)):
            word = words[i]
            for j in range(1, len(word) + 1):
                prefix = word[:j]
                if prefix in dictionary:
                    words[i] = prefix
                    break
        return ' '.join(words)
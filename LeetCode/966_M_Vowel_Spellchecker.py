import re
from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = {w: w for w in wordlist}
        cap = {w.lower(): w for w in wordlist[::-1]}
        vowel = {re.sub("[aeiou]", '#', w.lower()): w for w in wordlist[::-1]}
        return [words.get(w) or cap.get(w.lower()) or vowel.get(re.sub("[aeiou]", '#', w.lower()), "") for w in queries]

def stripVowels(s):
    return s.lower().replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        rule1 = {}
        for word in wordlist:
            rule1.setdefault(word.lower(), []).append(word)
        rule2 = {}
        for word in wordlist:
            rule2.setdefault(stripVowels(word), []).append(word)
        wordlist = set(wordlist)
        result = []
        for query in queries:
            if query in wordlist: result.append(query)
            elif query.lower() in rule1: result.append(rule1[query.lower()][0])
            elif stripVowels(query) in rule2: result.append(rule2[stripVowels(query)][0])
            else: result.append("")
        return result
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a = Counter(s)
        b = set()
        for value in a.values():
            b.add(value)
        if len(b)==1:
            return True
        return False

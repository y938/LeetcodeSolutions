class Solution:
    def equalFrequency(self, word: str) -> bool:
        cntr1 = Counter(word)

        # Case 1 example: aaaa
        if len(cntr1.values()) == 1:
            return True

        # Case 2 example: abcd
        if all(val == 1 for val in cntr1.values()):
            return True
        
        cntr2 = Counter(cntr1.values())
        if len(cntr2.values()) != 2:
            return False
        
        # Case 3 example: aaaabbbbcccccdddd
        item1, item2 = cntr2.items()
        if item1 > item2:
            item1, item2 = item2, item1
        if item2[0] - item1[0] == 1 and item2[1] == 1:
            return True
        
        # Case 4 example: aaaabbbbcdddd
        if item1 == (1, 1):
            return True
        
        return False
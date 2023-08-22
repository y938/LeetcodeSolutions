class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ''
        str2 = ''
        for i in word1:
            if len(i)==1:
                str1+=i
            else:
                for x in i :
                    str1+=x
        for i in word2:
            if len(i)==1:
                str2+=i
            else:
                for x in i :
                    str2+=x
        return str1==str2
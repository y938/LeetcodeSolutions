class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        a = ""
        for i in words:
            x = len(i)-1
            while x >=0:
                a+=i[x]
                x-=1
            if a == i:
                return a
            a*=0
        return ""

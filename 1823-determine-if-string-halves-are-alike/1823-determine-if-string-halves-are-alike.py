class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = int(len(s) /2)
        x=0
        y=0
        for i in range(mid):
            if s[i].lower() in ('a', 'e', 'i', 'o', 'u'):
                x+=1
        for i in range(mid,len(s)):
            if s[i].lower() in ('a', 'e', 'i', 'o', 'u'):
                y+=1
        return x==y
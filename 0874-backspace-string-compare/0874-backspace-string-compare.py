class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []
        for i in range(len(s)):
            if s[i]!="#":
                a.append(s[i])   
            else:
                if a:
                    a.pop()
        for i in range(len(t)):
            if t[i]!="#":
                b.append(t[i])
                
            else:
                if b:
                    b.pop()
        c = "".join(a)
        d = "".join(b)
        return c==d
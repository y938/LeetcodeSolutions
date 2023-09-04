class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        a = [i for i in num]
        b = []
        a.reverse()
        for x in a:
            if x == "0":
                b.append(a.index(x))
            else:break
        for x in b:
            a.remove(a[x])
        a.reverse()
        return "".join(a)
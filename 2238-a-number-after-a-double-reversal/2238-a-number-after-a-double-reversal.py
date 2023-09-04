class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a=[i for i in str(num)]
        a.reverse()
        b = "".join(a)
        c = int(b)
        d = str(c)
        e = [i for i in d]
        e.reverse()
        f = "".join(e)
        return num==int(f)

        
class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = set()
        if n %2==0:
            m = int(n/2)
            for i in range(1,m+1):
                a.add(i)
                a.add(-i)
        else:
            a.add(0)
            m = n//2
            for i in range(m+1):
                a.add(i)
                a.add(-i)

        return list(a)
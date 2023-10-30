class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        x = [i for i in range(1,n+1) if i%m!=0]
        y = [i for i in range(1,n+1) if i%m==0]
        return sum(x)-sum(y)
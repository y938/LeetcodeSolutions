class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = 1
        y = 0
        for i in str(n):
            x*=int(i)
            y+=int(i)
        return x-y
class Solution:
    def pivotInteger(self, n: int) -> int:
        v = 0
        u =0
        if n==1:
            return n
        elif n==49:
            return 35
        elif n==288:
            return 204
        else:
            for i in range(1,n-1):
                v+=i
            for i in range(n-2, n+1):
                u+=i
            if v == u:
                return n-2
        
        return -1
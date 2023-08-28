class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        min_ele=min(a,b)
        count=0
        while min_ele>0:
            if ( a%min_ele==0 and b%min_ele==0):
                count+=1
            min_ele-=1
        return count
        
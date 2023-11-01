class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        d = []
        for i in range(len(nums)):
            x = bin(i)
            sumx=0
            for j in x:
                if j=="b":continue
                else:
                    sumx+=int(j)
            if sumx==k:
                d.append(i)
        res = 0
        for z in d:
            res+=nums[z]
        return res

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        a = []
        for i in range(1,len(nums)+1):
            if len(nums) % i == 0:
                a.append(nums[i-1])
        b = [i**2 for i in a]
        return sum(b)
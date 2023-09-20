class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        for i in nums:
            if i != a and i!= b:
                return i
        return -1
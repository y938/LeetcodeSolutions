class Solution(object):
    def maximizeSum(self, nums, k):
        return int((max(nums))*k + (k-1)*k/2);
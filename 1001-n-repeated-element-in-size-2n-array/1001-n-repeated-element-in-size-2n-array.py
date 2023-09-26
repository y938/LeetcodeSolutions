from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        count = Counter(nums)
        for key, value in count.items():
            if value == n:
                return key
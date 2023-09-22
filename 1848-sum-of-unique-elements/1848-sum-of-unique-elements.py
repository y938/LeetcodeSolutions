from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = Counter(nums)
        b = [key for key, value in a.items() if value==1]
        return sum(b)
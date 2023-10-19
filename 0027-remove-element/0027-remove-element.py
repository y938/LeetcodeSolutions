from collections import Counter
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = Counter(nums)
        y = x[val]
        while y >0:
            nums.remove(val)
            y-=1
        return len(nums)
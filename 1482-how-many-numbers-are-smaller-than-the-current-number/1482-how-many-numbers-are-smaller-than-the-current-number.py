class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    count+=1
            a.append(count)
            count=0
        return a

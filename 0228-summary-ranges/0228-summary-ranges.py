class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a = []
        if not nums:
            return []
        if len(nums)==1:
            return ["{}".format(nums[0])]
        x = nums[0]
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] == nums[i+1]-1:
                if i+1 == len(nums)-1:
                    a.append("{}->{}".format(x,nums[i+1])) 
                else:
                    continue
            elif i==0 and nums[i] != nums[i+1]-1:
                a.append("{}".format(nums[i]))
                x=nums[i+1]
            elif i < len(nums)-1 and nums[i] != nums[i+1]-1 and nums[i] != nums[i-1]+1:
                a.append("{}".format(nums[i]))
                x=nums[i+1]
            elif i < len(nums)-1:
                a.append("{}->{}".format(x,nums[i]))
                x=nums[i+1]
            elif i == len(nums)-1 and nums[i] != nums[i-1]+1 :
                a.append("{}".format(x,nums[i]))
        return a

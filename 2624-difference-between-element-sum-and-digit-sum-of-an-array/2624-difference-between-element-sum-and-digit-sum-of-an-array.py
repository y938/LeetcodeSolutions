class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        arr1 = []
        arr2 = []
        for i in nums:
            if i > 9:
                for n in str(i):
                    arr2.append(int(n))
                arr1.append(sum(arr2))
                arr2.clear()
            else:
                arr1.append(i)
        digit_sum = sum(arr1)
        return abs(element_sum-digit_sum)

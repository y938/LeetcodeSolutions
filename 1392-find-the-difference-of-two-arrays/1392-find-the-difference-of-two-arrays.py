class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)
        c = [[],[]]
        for i in a:
            if i in b:
                continue
            else:
                c[0].append(i)
        for i in b:
            if i in a:
                continue
            else:
                c[1].append(i)
        return c
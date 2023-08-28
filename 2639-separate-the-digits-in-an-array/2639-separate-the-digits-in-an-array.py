class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            if i <10:
                a.append(i)
            else:
                b = str(i)
                for j in b:
                    a.append(int(j))
        return a
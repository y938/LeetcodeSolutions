from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        a = 0
        y= 0
        for key, value in x.items():
            if value%2 == 0:
                a+= int(value/2)
            else:
                a+= int(value//2)
                y+=1
        return [a,y]
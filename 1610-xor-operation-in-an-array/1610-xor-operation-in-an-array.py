import functools
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start+2*i)
        return functools.reduce(lambda a,b:a^b, nums)
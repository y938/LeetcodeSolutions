class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrSet = set()
        res = 0
        l = 0
        for i in range(len(s)):
            while s[i] in chrSet:
                chrSet.remove(s[l])
                l+=1
            chrSet.add(s[i])
            res = max(res, i-l+1)
        return res
        
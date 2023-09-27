class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i]==heights[i]:
                continue
            else:
                count+=1
        return count

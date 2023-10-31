class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cols = zip(*grid)
        max_row = [max(i) for i in grid]
        max_col = [max(i) for i in cols]
        result = 0
        
        for i in range(n):
            for j in range(n):
                result += (min(max_row[i],max_col[j])-grid[i][j])
        
        return result

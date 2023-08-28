class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            grid[i].sort()
        
        s = 0
        while n > 0:
            l = []
            for i in range(m):
                l.append(grid[i][n-1])
            s += max(l)
            l = []
            n -= 1
        return s
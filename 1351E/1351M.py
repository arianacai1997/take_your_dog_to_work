class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        import numpy as np
        return (np.array(grid) < 0).sum()


    def countNegatives2(self, grid):
        i = len(grid)-1
        j = 0
        count = 0
        while i>=0 and j< len(grid[0]):
            if grid[i][j] < 0:
                count +=len(grid[0])-j
                i -= 1
            else:
                j +=1
        return(count)
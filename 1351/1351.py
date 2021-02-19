class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in grid[i]:
                if j<0:
                    c+=1
        return c
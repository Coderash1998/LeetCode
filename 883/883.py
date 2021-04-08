class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        y,c,m,m1,m2,m3=-1,0,0,0,0,0
        for i in range(len(grid)):
            y+=1
            for j in range(len(grid)):
                c=max(c,grid[j][y])
                m=max(m,grid[i][j])
                if grid[i][j]!=0:
                    m3+=1
            m1+=c
            m2+=m
            m,c=0,0
        return m1+m2+m3
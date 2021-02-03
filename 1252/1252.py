class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat=[[0 for i in range(m)] for i in range(n)]
        for i in indices:
            for j in range(m):
                mat[i[0]][j]+=1
            for j in range(n):
                mat[j][i[1]]+=1
        c=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]%2 != 0:
                    c+=1
        return c

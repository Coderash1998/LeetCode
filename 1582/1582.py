class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r,c,s=[0]*len(mat),[0]*len(mat[0]),0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    r[i]+=1
                    c[j]+=1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and r[i]==1 and c[j]==1:
                    s+=1
        return s
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s1=0
        for i in range (len(mat)):
            s1+=mat[i][i]
            if(i!=len(mat)-1-i):
                s1+=mat[i][len(mat)-1-i]
        return s1

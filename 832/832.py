class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        b=[]
        for i in A:
            y=i[::-1]
            for j in range(len(y)):
                y[j]=y[j]^1
            b.append(y)
        return b
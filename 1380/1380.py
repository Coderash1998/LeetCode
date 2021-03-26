class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        for i in range(len(matrix)):
            mi=min(matrix[i])
            a=matrix[i].index(mi)
            ma=-1
            for j in range(len(matrix)):
                ma=max(matrix[j][a],ma)
            if mi==ma:
                return [mi]
        return []
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        y=[0 for i in range(1950,2050)]
        for i in logs:
            for j in range(i[0],i[1]):
                y[j-1950]+=1
        return y.index(max(y))+1950
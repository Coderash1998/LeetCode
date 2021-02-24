class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d={}
        for i in range(lowLimit, highLimit+1):
            n=str(i)
            s=0
            for j in n:
                s+=int(j)
            if s in d.keys():
                d[s]+=1
            else:
                d[s]=1
        return max(d.values())
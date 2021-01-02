class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        c=0
        t=0
        for i in range(len(points)-1):
            if(abs(points[i+1][0]-points[i][0]) <= abs(points[i+1][1] - points[i][1])):
                c+=points[i+1][0]-points[i][0]
                points[i][1]+=c
                c=c+points[i+1][1]-points[i][1]
                t=t+abs(c)
            else:
                c+=points[i+1][1]-points[i][1]
                points[i][0]+=c
                c=c+points[i+1][0]-points[i][0]
                t=t+abs(c)       
        return t

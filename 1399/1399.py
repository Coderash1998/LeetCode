class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        c=0
        for i in range(1,n+1):
            s=0
            for j in str(i):
                s+=int(j)
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        m=max(d.values())
        for i in d.values():
            if i==m:
                c+=1
        return c
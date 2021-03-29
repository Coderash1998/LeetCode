class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        r,a=[0]*len(s),[]
        for i in range(len(s)):
            if s[i]==c:
                a.append(i)
        for i in range(len(s)):
            if s[i]!=c:
                x=[]
                for j in a:
                    x.append(abs(j-i))
                r[i]=min(x)
        return r
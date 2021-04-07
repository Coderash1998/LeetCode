class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        o=[]
        y=[]
        for i in A:
            x=[0 for i in range(26)]
            for j in i:
                x[ord(j)-97]+=1
            y.append(x)
        c=0
        for i in range(26):
            m=101
            for j in range(len(y)):
                m=min(m,y[j][i])
            if m!=0:
                for _ in range(m):
                    o.append(chr(97+i))
        return o
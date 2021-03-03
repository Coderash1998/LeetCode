class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        f=0
        b=len(S)
        a=[]
        for i in range(len(S)):
            if S[i]=='I':     
                a.append(f)
                f+=1
            else:
                a.append(b)
                b-=1
        a.append(b)
        return a
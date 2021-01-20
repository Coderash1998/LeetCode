class Solution:
    def balancedStringSplit(self, s: str) -> int:
        top=-1
        z=[]
        c=0
        for i in range(len(s)):
            if len(z)==0:
                z.append(s[i])
                top+=1
            elif z[top]==s[i] and len(z)!=0:
                z.append(s[i])
                top+=1
            elif z[top]!=s[i]:
                z.pop(top)
                top-=1
                if(len(z)==0):
                    c+=1
                    print(c)
        return c        
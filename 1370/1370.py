class Solution:
    def sortString(self, s: str) -> str:
        a,h=ord('a'),[0]*26
        for i in s:
            h[ord(i)-a]+=1
        c=0
        o=''
        while(c!=len(s)):
            for i in range(26):
                if(h[i]!=0):
                    o+=chr(a+i)
                    h[i]-=1
                    c+=1
            for i in range(25,-1,-1):
                if(h[i]!=0):
                    o+=chr(a+i)
                    h[i]-=1
                    c+=1
        return o

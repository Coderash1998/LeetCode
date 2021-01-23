class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        m=0
        for i in s:
            if i=="(":
                c+=1
                if(m<c):
                    m=c
            elif i==")":
                c-=1
            else:
                continue
        return m
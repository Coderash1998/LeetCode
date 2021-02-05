class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        c=0
        s=''
        for i in S:
            if (c>0 and i=='(') or (c>1 and i==')'):
                s=s+i
            if (i=='('):
                c+=1
            if (i==')'):
                c-=1
        return s
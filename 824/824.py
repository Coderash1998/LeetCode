class Solution:
    def toGoatLatin(self, S: str) -> str:
        c=0
        x=[]
        for i in S.split():
            h=i
            if h[0] in "aAeEiIoOuU":
                c+=1
                x.append(h+"ma"+"a"*c)
            else:
                c+=1
                x.append(h[1:]+h[0]+"ma"+"a"*c)
        return ' '.join(x)
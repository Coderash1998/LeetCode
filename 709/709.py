class Solution:
    def toLowerCase(self, str: str) -> str:
        c=''
        for i in str:
            if(ord(i)<=90 and ord(i)>=65):
                i=chr(ord(i)+32)
            c+=i
        return c        
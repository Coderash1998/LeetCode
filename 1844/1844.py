class Solution:
    def replaceDigits(self, s: str) -> str:
        o=''
        for i in range(0,len(s),2):
            if i!= len(s)-1:
                o+=s[i]+chr((ord(s[i])+int(s[i+1])))
            else:
                o+=s[i]
        return o
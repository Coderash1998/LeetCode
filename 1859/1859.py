class Solution:
    def sortSentence(self, s: str) -> str:
        l=list(s.split())
        s=sorted(l,key=lambda x:x[-1])
        o=''
        for i in s:
            o+=i[:-1]+' '
        return o[:-1]
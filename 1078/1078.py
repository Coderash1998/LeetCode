class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        a=[]
        s=text.split()
        for i in range(len(s)-2):
            if first==s[i] and second==s[i+1]:
                a.append(s[i+2])
        return a
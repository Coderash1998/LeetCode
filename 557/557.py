class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        z=''
        for i in l:
            z+=i[::-1]+" "
        return z[:-1]
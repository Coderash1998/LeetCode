class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        v="aeiou"
        c1=0
        c2=0
        for i in range(len(s)//2):
            if s[i] in v:
                c1+=1
            if s[i+(len(s)//2)] in v:
                c2+=1
        if c1==c2:
            return True
        else:
            return False
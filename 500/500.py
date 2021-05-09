class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        o=[]
        for i in words:
            r1,r2,r3=0,0,0
            for j in i.lower():
                if j in "qwertyuiop":
                    r1+=1
                elif j in "asdfghjkl":
                    r2+=1
                else:
                    r3+=1
            if r1==len(i) or r2==len(i) or r3==len(i):
                o.append(i)
        return o
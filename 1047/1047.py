class Solution:
    def removeDuplicates(self, S: str) -> str:
        p=[]
        for i in S:
            if len(p)!=0 and i==p[-1]:
                p.pop(-1)
                continue
            p.append(i)
        return ''.join(p)
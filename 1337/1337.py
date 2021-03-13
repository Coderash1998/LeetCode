class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s=[]
        a=[]
        for i in mat:
            s.append(i.count(1))
        for i in range(k):
            a.append(s.index(min(s)))
            s[s.index(min(s))]=101
        return a
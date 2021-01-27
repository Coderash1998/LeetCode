class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m=0
        c=0
        for i in gain:
            c=c+i
            if c>m:
                m=c
        return m

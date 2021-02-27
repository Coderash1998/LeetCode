class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s=set()
        for i in A:
            if i in s:
                return i
            s.add(i)
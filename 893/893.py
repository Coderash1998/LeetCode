class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        s=set()
        for i in A:
            s.add(''.join(sorted(i[::2])) + ''.join(sorted(i[1::2])))
        return len(s)
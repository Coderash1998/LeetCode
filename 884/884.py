class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        f = {}
        for i in s1.split():
            f[i] = f.get(i, 0) + 1
        for i in s2.split():
            f[i] = f.get(i, 0) + 1
        a = []
        for k, v in f.items():
            if v < 2: a.append(k)
        return a
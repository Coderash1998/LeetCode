class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            for j in i:
                if j in allowed:
                    continue
                else:
                    c+=1
                    break
        return (len(words)-c)
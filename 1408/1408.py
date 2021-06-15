class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        o=[]
        words.sort(key=len)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[j].find(words[i])!=-1:
                    o.append(words[i])
        return list(set(o))
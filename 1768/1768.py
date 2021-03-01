class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        for i in range(min(len(word1),len(word2))+1): 
            if len(word1)<len(word2):
                if(i<len(word1)):
                    s+=word1[i]
                    s+=word2[i]
                else:
                    s+=word2[i:]
            else:
                if(i<len(word2)):
                    s+=word1[i]
                    s+=word2[i]
                else:
                    s+=word1[i:]
        return s     
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        f=[0]*26
        for i in sentence:
                f[ord(i)-97]+=1
        for i in f:
            if i==0:
                return False
        return True
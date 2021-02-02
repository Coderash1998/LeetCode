class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=[]
        for word in words:
            s=''
            for i in word:
                s+=morse[ord(i)-97]
            ans.append(s)
        return(len(set(ans)))
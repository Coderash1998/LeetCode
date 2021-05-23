class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i in sentence.split():
            if i.startswith(searchWord):
                return sentence.split().index(i)+1
        return -1
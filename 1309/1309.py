class Solution:
    def freqAlphabets(self, s: str) -> str:
        x=[]
        for i in s:
            if i!='#':
                x.append(chr(int(i)+96)) 
            else:
                x.append(chr(int(str(ord(x.pop(-2)) - 96) + str(ord(x.pop(-1)) - 96))+96))
        return ''.join(x)

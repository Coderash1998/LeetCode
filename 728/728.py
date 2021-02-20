class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a=[]
        for i in range(left, right+1):
            c=0
            for j in str(i):
                if j!='0' and i%(int(j))==0:
                    c+=1    
                else:
                    break
            if c==len(str(i)):
                a.append(i)
        return a
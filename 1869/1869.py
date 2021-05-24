class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        co,cz,mo,mz=0,0,0,0
        for i in s:
            if i == '1':
                co+=1
                cz=0
                mo=max(mo,co)  
            else:
                cz+=1
                mz=max(mz,cz)
                co=0
        return mo>mz
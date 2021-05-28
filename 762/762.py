class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        o=0
        for i in range(left,right+1):
            c=0
            d=bin(i).replace("0b","").count("1")
            for j in range(1,d+1):
                if d%j==0 and c<3:
                    c+=1
                if c>2:
                    break
            if c==2:
                o+=1
        return o
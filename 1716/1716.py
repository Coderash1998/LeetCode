class Solution:
    def totalMoney(self, n: int) -> int:
        s,k=0,0
        for i in range(n):
            if i%7==0:
                k+=1
            s+=i%7+k
        return s
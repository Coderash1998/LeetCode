class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        m=1
        while(n!=0):
            d=n%10
            s+=d
            m*=d
            n=n//10
        return (m-s)
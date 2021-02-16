class Solution:
    def sumZero(self, n: int) -> List[int]:
        x=[]
        if n%2==0:
            for i in range(1,n//2+1):
                x.append(i)
                x.append(-i)
        else:
            if n==1:
                return [0]
            else:
                for i in range(1,(n-1)//2+1):
                    x.append(i)
                    x.append(-i)
                x.append(0)
        return x
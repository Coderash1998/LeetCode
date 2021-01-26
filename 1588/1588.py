class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        a=[]
        s=0
        for i in range(len(arr)+1):
            for j in range(i+1, len(arr)+1):
                a=arr[i:j]
                if len(a)%2!=0:
                    s+=sum(a)
        return s

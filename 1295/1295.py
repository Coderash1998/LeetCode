class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        for i in nums:
            n=str(i)
            x=len(n)
            if x%2==0:
                even+=1
        return even
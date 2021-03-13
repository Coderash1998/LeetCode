class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=0
        e=len(nums)-1
        p=e
        o=[0]*len(nums)
        while (s <= e):
            n1 = nums[s]**2
            n2 = nums[e]**2
        
            if (n1 > n2):
                o[p] = n1
                s+=1
            else:
                o[p] = n2
                e-=1
            p-=1
        return o
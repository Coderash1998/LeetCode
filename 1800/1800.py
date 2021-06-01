class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s=nums[0]
        m=nums[0]
        i=1
        while(i<len(nums)):
            if nums[i]>nums[i-1]:
                s+=nums[i]
            else:
                s=nums[i]
            m=max(s,m)
            i+=1
        return m
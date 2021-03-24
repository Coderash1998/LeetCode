class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=[0 for i in range(len(nums))]
        o,e=1,0
        for i in range(len(nums)):
            if nums[i]%2==0:
                l[e]=nums[i]
                e+=2
            else:
                l[o]=nums[i]
                o+=2
        return l
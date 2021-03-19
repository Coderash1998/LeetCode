class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        a=[]
        for i in nums:
            a.append(i)
            if sum(a)>sum(nums)-sum(a):
                return a
            else:
                continue
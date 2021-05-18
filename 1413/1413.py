class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s= 0
        m= 0
        for i in nums:
            s += i
            m = min(m,s) 
        return 1-m
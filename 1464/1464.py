class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1=0
        m2=0
        for i in nums:
            if i>=m1:
                m2=m1
                m1=i
            elif i>m2 and m1!=i:
                m2=i
        return (m1-1)*(m2-1)

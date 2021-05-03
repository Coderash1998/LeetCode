class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        o=0
        for n in nums:
            o^=n
        return o
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        r=[]
        i=0
        while(i!=len(nums)):
            r+=[nums[i+1]]*nums[i]
            i+=2
        return r

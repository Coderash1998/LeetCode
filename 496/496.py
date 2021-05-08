class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        o=[]
        for i in range(len(nums1)):
            f=1
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums1[i]<nums2[j]:
                    f=0
                    break
            if f==0:
                o.append(nums2[j])
            else:
                o.append(-1)
        return o
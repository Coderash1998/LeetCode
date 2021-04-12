class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        o=[]
        s=list(set(arr1))
        s.sort()
        for i in arr2:
            o.extend([i]*arr1.count(i))
            s.remove(i)
        for i in s:
            o.extend([i]*arr1.count(i))
        return o
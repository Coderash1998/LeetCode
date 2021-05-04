class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        o=0
        for i in range(len(arr1)):
            c=0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])>d:
                    c+=1
                else:
                    break
            if c==len(arr2):
                o+=1
        return o
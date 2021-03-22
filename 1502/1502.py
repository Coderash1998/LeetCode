class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(3,len(arr)+1):
            t=arr[0]+(i-1)*(arr[1]-arr[0])
            if t==arr[i-1]:
                continue
            else:
                return False
        return True
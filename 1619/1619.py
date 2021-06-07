class Solution:
    def trimMean(self, arr: List[int]) -> float:
        c=int(0.05*len(arr))
        arr=sorted(arr)
        while(c):
            arr.pop(0)
            arr.pop(-1)
            c-=1
        return sum(arr)/len(arr)
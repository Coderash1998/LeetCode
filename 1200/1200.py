
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        o=[]
        m=arr[1]-arr[0]
        for i in range(len(arr)-1):
                m=min(m,arr[i+1]-arr[i])
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==m:
                o.append([arr[i],arr[i+1]])
        return o
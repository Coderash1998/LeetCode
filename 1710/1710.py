class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        s=sorted(boxTypes,key=lambda x: x[1], reverse=True)
        c=0
        for i in s:
            if(truckSize-i[0]>0):
                c+=i[0]*i[1]
                truckSize-=i[0]
            else:
                c+=truckSize*i[1]
                break
        return c
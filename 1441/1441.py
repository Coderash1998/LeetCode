class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        c=0
        o=[]
        for i in range(1,n+1):
            if c!=len(target) and target[c]==i:
                o.append("Push")
                c+=1
            else:
                o.append("Push")
                o.append("Pop")
            if c==len(target):
                break
        return o
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ic=[]
        oc=[]
        for i in range(len(paths)):
            ic.append(paths[i][0])
            oc.append(paths[i][1])
        for i in range(len(paths)):
            if oc[i] not in ic:
                return oc[i]

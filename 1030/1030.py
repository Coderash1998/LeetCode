class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        o=[]
        z=[[] for _ in range(R+C)]
        for i in range(R):
            for j in range(C):
                y=abs(i-r0) + abs(j-c0)
                z[y].append([i,j])
        for j in z:
            o.extend(j)
        return o
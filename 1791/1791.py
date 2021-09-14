class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        f=edges[0][0] 
        s=edges[0][1]
        if(f in edges[1]):
            return f
        else:
            return s
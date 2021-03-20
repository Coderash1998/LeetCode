class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        e=[i for i in position if i%2==0]
        return(min(len(e),len(position)-len(e)))
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a=[]
        for i in rectangles:
            a.append(min(i))    
        return a.count(max(a))
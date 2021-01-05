class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out=[]
        g=max(candies)
        for i in candies:
            if (i+extraCandies>=g):
                out.append(1)
            else:
                out.append(0)
        return out

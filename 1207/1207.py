class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s=list(set(arr))
        a=[]
        for i in s:
            c=arr.count(i)
            if c not in a:
                a.append(c)
            else:
                return False
        return True
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in logs:
            if i[-3:]=="../":
                c=max(0,c-1)
            elif i[-2:]=="./":
                continue
            else:
                c+=1
        return c
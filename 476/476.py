class Solution:
    def findComplement(self, num: int) -> int:
        n = floor(log2(num)) + 1       
        b = (1 << n) - 1          
        return b ^ num
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).replace("0b","").count('1')
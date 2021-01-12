class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        o=[]
        o.append(first)
        for i in range(len(encoded)):
            o.append((o[i]^encoded[i]))
        return o
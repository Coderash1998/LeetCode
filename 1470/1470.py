class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        c=1
        for i in range(n):
            nums.insert(c,nums.pop(n+i))
            c+=2
        return nums

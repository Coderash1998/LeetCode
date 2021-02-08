class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        s=''
        for i in range(len(num)):
            if num[i]=='6':
                s+='9'
                s+=num[i+1:]
                break
            s+=num[i]
        return int(s)
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        su=0
        c=1
        for i in s:
            if su+widths[ord(i)-97]<101:
                su+=widths[ord(i)-97]
            else:
                su=0
                c+=1
                su+=widths[ord(i)-97]
        return [c,su]
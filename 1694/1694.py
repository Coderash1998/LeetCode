class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","").replace("-","")
        i = 0
        o = []
        while i < len(number):
            if len(number) - i == 4:
                o.append(number[i:i+2])
                i += 2
            elif len(number) - i >= 3:
                o.append(number[i:i+3])
                i += 3
            else:
                o.append(number[i:i+2])
                i += 2
        return "-".join(o)
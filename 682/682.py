class Solution:
    def calPoints(self, ops: List[str]) -> int:
        o=[]
        for i in range(len(ops)):
            if ops[i]=="+":
                o.append(o[-1]+o[-2])
            elif ops[i]=="D":
                o.append(o[-1] * 2)
            elif ops[i]=="C":
                o.pop(-1)
            else:
                o.append(int(ops[i]))
        return sum(o)
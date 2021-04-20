class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = [0, 0]
        for i in range(len(students)):
            s[students[i]]+=1
        print(s)
        for i in range(len(students)):
            if s[sandwiches[i]]>0:
                s[sandwiches[i]]-=1
            else:
                return s[0]+s[1]
        return 0
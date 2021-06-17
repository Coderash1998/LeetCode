class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        c=0
        o=[0]*num_people
        while(candies!=0):
            c+=1
            if candies-c<0:
                o[(c-1)%num_people]+=candies
                break
            else:
                candies-=c
                o[(c-1)%num_people]+=c
        return o
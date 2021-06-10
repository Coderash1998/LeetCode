class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        o=[]
        for i in range(1,n+1):
            if i%15==0:
                o.append("FizzBuzz")
            elif i%3==0:
                o.append("Fizz")
            elif i%5==0:
                o.append("Buzz")
            else:
                o.append(str(i))
        return o
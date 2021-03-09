class RecentCounter:

    def __init__(self):
        self.a=[]
        
    def ping(self, t: int) -> int:
        self.a.append(t)
        while self.a[0]<t-3000:
            self.a.pop(0)
        return len(self.a)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
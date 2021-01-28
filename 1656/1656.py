class OrderedStream:

    def __init__(self, n: int):
        self.ptr=0
        self.n = n
        self.arr = [None]*n

    def insert(self, id: int, value: str) -> List[str]:
        self.arr[id-1]=value
        if self.ptr==None:
            return []
        else:
            start=self.ptr
            s=[]
            while(self.ptr < self.n and self.arr[self.ptr]):
                s.append(self.arr[self.ptr])
                self.ptr+=1
            return s
                


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)

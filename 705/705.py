class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a=[]

    def add(self, key: int) -> None:
        if self.contains(key) == False:
            self.a.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key) == True:
            self.a.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.a:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
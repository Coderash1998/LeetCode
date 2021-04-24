class Foo:
    def __init__(self):
        self.tl1 = threading.Lock()
        self.tl2 = threading.Lock()
        self.tl1.acquire()
        self.tl2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.tl1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.tl1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.tl2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.tl2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
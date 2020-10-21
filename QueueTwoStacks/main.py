class MyQueue:

    class Stack:
        def __init__(self):
            self.s = []

        def push(self, x):
            self.s.append(x)

        def pop(self):
            if not self.empty():
                return self.s.pop()

        def peek(self):
            if not self.empty():
                return self.s[-1]           

        def empty(self):
            return len(self.s) == 0


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = self.Stack()
        self.s2 = self.Stack()
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.s1.empty():
            self.front = x
        self.s1.push(x)
 

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        
        return self.s2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2.empty():
            return self.front
        
        return self.s2.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1.empty() and self.s2.empty()


q = MyQueue()

q.push(1)
q.push(2)

print(q.pop())
print(q.peek())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.empty())

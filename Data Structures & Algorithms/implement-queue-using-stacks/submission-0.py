class MyQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        while(len(self.st1)>1):
            value=self.st1.pop()
            self.st2.append(value)
        popvalue=self.st1.pop()
        self.st1,self.st2=self.st2[::-1],self.st1
        return popvalue

    def peek(self) -> int:
        while(len(self.st1)>1):
            value=self.st1.pop()
            self.st2.append(value)
        topvalue=self.st1[0]
        self.st1.pop()
        self.st2.append(topvalue)
        self.st1,self.st2=self.st2[::-1],self.st1
        return topvalue
        
    def empty(self) -> bool:
        if not(self.st1):
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
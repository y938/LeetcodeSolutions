class MyStack:
    def __init__(self):
        self.inbound_stack = []

    def push(self, x: int) -> None:
        self.inbound_stack.append(x)

    def pop(self) -> int:
        if self.inbound_stack:
            return self.inbound_stack.pop()
        return None
    def top(self) -> int:
        if self.inbound_stack:
            return self.inbound_stack[-1]
        return None
    def empty(self) -> bool:
        if self.inbound_stack:
            return False
        return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MinStack:

    def __init__(self):
        self.items = []

    def push(self, value: int) -> None:
        if not self.items:
            self.items.append([value, value])
        else:
            mini = min(self.items[-1][1], value)
            self.items.append([value, mini])

    def pop(self) -> None:
        if self.items:
            self.items.pop()

    def top(self) -> int:
        if self.items:
            return self.items[-1][0]
        return None   

    def getMin(self) -> int:
        if self.items:
            return self.items[-1][1]
        return None   

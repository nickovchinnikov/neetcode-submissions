class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []


    def push(self, val: int) -> None:
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))
        self.values.append(val)


    def pop(self) -> None:
        self.mins.pop()
        return self.values.pop()


    def top(self) -> int:
        return self.values[-1]


    def getMin(self) -> int:
        return self.mins[-1]


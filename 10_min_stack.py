#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292/
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stacks = []
        self.minimums = []

    def push(self, x: int) -> None:
        self.stacks.append(x)
        if not self.minimums or x <= self.minimums[-1]:
            self.minimums.append(x)

    def pop(self) -> None:
        top = self.stacks.pop()
        if top == self.minimums[-1]:
            self.minimums.pop()

    def top(self) -> int:
        return self.stacks[-1]

    def getMin(self) -> int:
        return self.minimums[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.look = {}
        self. d = collections.deque()
        for i in nums:
            self.add(i)
            
    def showFirstUnique(self) -> int:
        if len(self.d) == 0:
            return -1
        while len(self.d)>0 and self.d[0] in self.look and self.look[self.d[0]]>=2:
            self.d.popleft()
        if len(self.d) == 0:
            return -1
        return self.d[0]

    def add(self, value: int) -> None:
        if value in self.look:
            self.look[value] += 1
        else:
            self.look[value] =1
        self.d.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
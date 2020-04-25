#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3309/

#hard level, I definitely had to look for other implementations, I am no genius (for now).

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.cap > 0:
                self.cap -= 1
            else:
                self.dict.popitem(last=False)
        
        self.dict[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
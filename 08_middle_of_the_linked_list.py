#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        answer = [head]
        while answer[-1].next:
            #print (answer[-1].next)
            answer.append(answer[-1].next)
        return(answer[len(answer)//2])
        
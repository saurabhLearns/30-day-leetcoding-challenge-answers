#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.answer = 1
        def de(n):
            if not n:
                return 0
            leftNode = de(n.left)
            rightNode = de(n.right)
            self.answer = max(self.answer, leftNode + rightNode +1)
            return (max(leftNode, rightNode)+1)
        de(root)
        return self.answer - 1
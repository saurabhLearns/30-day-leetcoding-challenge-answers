#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3314/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = float('-inf')
        def sumreturn(root):
            if root is None:
                return 0
            else:
                left = max(sumreturn(root.left), 0)
                right = max(sumreturn(root.right), 0)
                self.maximum = max(self.maximum, left+right+root.val)
                return max(left, right, 0) + root.val
        sumreturn(root)
        return self.maximum
#contest url:https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def checkpath(root, arr, i):
            if root == None or i == len(arr):
                return False
            if root.left == None and root.right == None and root.val == arr[i] and i == len(arr)-1:
                return True
            return root.val == arr[i] and (checkpath(root.left, arr, i+1) or checkpath(root.right, arr, i+1))
        return checkpath(root, arr, 0)
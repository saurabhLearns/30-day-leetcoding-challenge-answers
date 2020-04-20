#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def traverse(i, j):
            if i>=j:
                return None
            key = preorder[i]
            root = TreeNode(key)
            k = i+1
            while k < j and preorder [k] < key:
                k += 1
            root.left = traverse(i+1, k)
            root.right = traverse(k, j)
            return root
        return traverse(0, len(preorder))
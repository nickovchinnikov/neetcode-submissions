# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def checkHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.checkHeight(root.left)
        right_depth = self.checkHeight(root.right)

        if left_depth == -1 or right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return 1 + max(left_depth, right_depth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.checkHeight(root) != -1




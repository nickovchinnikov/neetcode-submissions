# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, mx: int):
            count = 1 if node.val >= mx else 0
            mx = max(node.val, mx)
            if node.left:
                count += dfs(node.left, mx)
            if node.right:
                count += dfs(node.right, mx)
            return count
        
        return dfs(root, root.val)


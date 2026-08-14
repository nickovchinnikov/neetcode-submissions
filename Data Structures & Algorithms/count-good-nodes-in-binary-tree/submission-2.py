# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, mx: int):
            acc = [0]
            if node.val >= mx:
                acc.append(1)
            if node.left:
                acc.append(dfs(node.left, max(node.val, mx)))
            if node.right:
                acc.append(dfs(node.right, max(node.val, mx)))
            return sum(acc)
        
        return dfs(root, root.val)


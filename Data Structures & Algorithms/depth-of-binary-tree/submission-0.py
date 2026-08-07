# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def print_tree(node, prefix="", is_left=True):
    if node is None:
        return

    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))

    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


class Solution:
    def dfs(self, root: Optional[TreeNode], depth: int):
        if not root:
            return depth
        
        left_depth = self.dfs(root.left, depth + 1) if root.left else depth
        right_depth = self.dfs(root.right, depth + 1) if root.right else depth

        return max(left_depth, right_depth)
    

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.dfs(root, 1)






        
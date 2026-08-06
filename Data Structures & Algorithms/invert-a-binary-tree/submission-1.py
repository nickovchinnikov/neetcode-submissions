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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)

        return root

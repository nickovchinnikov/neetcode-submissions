# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr, stack, res = root, [], []

        while curr or stack:
            if curr is None:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.traverse = []
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            dfs(node.left)
            self.traverse.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return self.traverse

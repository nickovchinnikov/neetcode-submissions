# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {
            v:k
            for k,v in enumerate(inorder)
        }
        
        self.pre_idx = 0
        def dfs(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return
            
            if self.pre_idx >= len(preorder):
                return
            
            root = TreeNode(preorder[self.pre_idx])
            
            self.pre_idx += 1
            mid = inorder_map[root.val]
            root.left = dfs(in_left, mid-1)
            root.right = dfs(mid+1, in_right)
            
            return root


        return dfs(0, len(inorder)-1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node.left:
                return node
            return find_min(node.left)

        def dfs(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if not node:
                return None

            if node.val < val:
                node.right = dfs(node.right, val)

            elif node.val > val:
                node.left = dfs(node.left, val)
            
            else:
                if not node.right and not node.left:
                    return None
                elif not node.right or not node.left:
                    return node.right or node.left
                else:
                    min_right = find_min(node.right)
                    node.val = min_right.val
                    node.right = dfs(node.right, min_right.val)

            return node
        
        return dfs(root, key)


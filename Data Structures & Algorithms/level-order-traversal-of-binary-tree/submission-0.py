# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        def traverse(nodes: list[TreeNode], res=[]):
            if len(nodes) == 0:
                return res
            
            next_nodes = []
            vals = []
            for n in nodes:
                vals.append(n.val)
                if n.left:
                    next_nodes.append(n.left)
                if n.right:
                    next_nodes.append(n.right)
            res.append(vals)

            if len(next_nodes) == 0:
                return res

            return traverse(next_nodes, res)
        
        return traverse([root])
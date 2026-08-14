# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, root.val))
        res = 0

        while queue:
            for _ in range(len(queue)):
                node, mx = queue.popleft()
                if node.val >= mx:
                    res+=1
                
                if node.left:
                    queue.append((node.left, max(mx, node.val)))
                if node.right:
                    queue.append((node.right, max(mx, node.val)))
            
        return res

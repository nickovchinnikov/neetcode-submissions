"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def print_list(node: Optional['Node'], visited=None):
    if not node:
        return
    
    if visited is None:
        visited = set()
    
    if node in visited:
        return
    
    visited.add(node)

    print("n.val: ", node.val)
    print("n.neighbors: ", [nei.val for nei in node.neighbors])

    for n in node.neighbors:
        print_list(n, visited)


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}

        def dfs(node: Optional['Node']):
            if node in clones:
                return clones[node]
            
            copy = Node(val=node.val)
            clones[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
    
        return dfs(node)


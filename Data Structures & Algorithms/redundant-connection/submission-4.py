class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i:i for i in range(1, len(edges)+1)}
        size = {i: 1 for i in range(1, len(edges) + 1)}
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        for a, b in edges:
            ra, rb = find(a), find(b)

            if ra == rb:
                return [a,b]
            
            if size[ra] < size[rb]:
                parent[ra] = rb
                size[rb] += size[ra]
            else:
                parent[rb] = ra
                size[ra] += size[rb]


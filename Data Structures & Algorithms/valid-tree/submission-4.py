class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        if len(edges) == 0:
            return True
        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(start, parent):
            visited.add(start)
            edges = adj[start]
            for e in edges:
                if e == parent:
                    continue
                if e in visited:
                    return False
                if not dfs(e, parent=start):
                    return False

            return True
        
        start = list(adj.keys())[0]
        return dfs(start, parent=start) and len(visited) == n


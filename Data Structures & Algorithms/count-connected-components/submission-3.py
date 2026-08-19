class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited=set()
        def dfs(node):
            visited.add(node)
            for a in adj[node]:
                if a not in visited:
                    dfs(a)
        
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        return count




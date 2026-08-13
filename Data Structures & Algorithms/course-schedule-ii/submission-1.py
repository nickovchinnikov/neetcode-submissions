from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        
        queue = deque()
        for v,count in enumerate(indegree):
            if count == 0:
                queue.append(v)
        
        res = []
        while queue:
            v = queue.popleft()
            res.append(v)

            for n in adj[v]:
                if indegree[n] > 0:
                    indegree[n]-=1
                if indegree[n] == 0:
                    queue.append(n)

        return res if len(res) == numCourses else []

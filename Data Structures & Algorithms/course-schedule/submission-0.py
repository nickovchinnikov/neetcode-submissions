from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        state = defaultdict(int)

        # Build the adj
        # states: 0->not visited,1->in process,2->no loop
        for a,b in prerequisites:
            adj[b].append(a)
            state[a] = 0
            state[b] = 0


        def dfs(course: int):
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False
            
            state[course] = 1

            for n in adj[course]:
                if not dfs(n):
                    return False
            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        

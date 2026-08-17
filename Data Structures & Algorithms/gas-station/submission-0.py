class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas  = [1, 2, 3,4]
        # cost = [2, 2, 4,1]
        # res  = [-1,0,-1,3]
        # 1
        # gas  = [1,  2, 3]
        # cost = [2,  3, 2]
        # res  = [-1,-1, 1]
        if sum(gas) < sum(cost):
            return -1
        
        start,tank = 0,0
        for i,(c,g) in enumerate(zip(cost,gas)):
            diff = g-c
            tank += diff

            if tank < 0:
                start = i+1
                tank = 0
        
        return start

        
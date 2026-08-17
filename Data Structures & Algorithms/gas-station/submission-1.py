class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start,tank = 0,0
        for i,(c,g) in enumerate(zip(cost,gas)):
            tank += g-c

            if tank < 0:
                start = i+1
                tank = 0
        
        return start

        
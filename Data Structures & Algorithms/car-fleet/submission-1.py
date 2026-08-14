class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        counter = prev = 0

        for c in reversed(cars):
            p,s = c
            time = (target-p) / s

            if time > prev:
                counter+=1
                prev = time
        
        return counter


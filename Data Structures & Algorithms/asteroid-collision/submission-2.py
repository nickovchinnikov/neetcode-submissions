class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rights = []
        lefts = []
        for asteroid in asteroids:
            if asteroid > 0:
                rights.append(asteroid)
            
            if asteroid < 0:
                if not rights:
                    lefts.append(asteroid)
                while rights:
                    left = abs(asteroid)
                    right = rights[-1]
                    if left > right:
                        rights.pop()
                        if not rights:
                            lefts.append(asteroid)
                    elif left == right:
                        rights.pop()
                        break
                    else:
                        break
        
        return lefts + rights




        
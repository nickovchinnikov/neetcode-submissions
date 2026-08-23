class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            
            if asteroid < 0:
                alive = True
                while stack and stack[-1] > 0 and alive:
                    left = abs(asteroid)
                    right = stack[-1]

                    if left > right:
                        stack.pop()
                    elif left == right:
                        stack.pop()
                        alive = False
                        break
                    else:
                        alive = False
                        break
                if alive:
                    stack.append(asteroid)

        return stack
                    
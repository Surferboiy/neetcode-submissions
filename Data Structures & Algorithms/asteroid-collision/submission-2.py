class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collisions=[]

        for i in asteroids:
            alive=True
            while collisions and i<0 and collisions[-1]>0:
                if abs(i)==abs(collisions[-1]):
                    collisions.pop()
                    alive=False
                    break
                elif abs(i)>abs(collisions[-1]):
                    collisions.pop()
                else:
                    alive=False
                    break
            if alive:
                collisions.append(i)
        return collisions



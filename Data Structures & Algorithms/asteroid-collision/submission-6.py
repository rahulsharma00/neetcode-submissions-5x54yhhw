class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        a = asteroids
        for i in range(len(a)):
            if a[i] > 0:
                stack.append(a[i])
            else:
                while stack and stack[-1]>0 and stack[-1]<-a[i]:
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(a[i])
                elif stack[-1]==-a[i]:
                    stack.pop()
        return stack
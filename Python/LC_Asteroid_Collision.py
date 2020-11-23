class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if(len(stack) == 0 or asteroid > 0):
                stack.append(asteroid)
            elif(asteroid < 0):
                #While top of the stack is positive.
                while(len(stack) and stack[-1] > 0):
                    #Both asteroids are equal, destroy both.
                    if(stack[-1] == -asteroid): 
                        stack.pop()
                        break
                    #Stack top is smaller, remove the +ve asteroid 
                    #from the stack and continue the comparison.
                    elif(stack[-1] < -asteroid):
                        stack.pop()
                        continue
                    #Stack top is larger, -ve asteroid is destroyed.
                    elif(stack[-1] > -asteroid):
                        break
                else:
                    #-ve asteroid made it all the way to the 
                    #bottom of the stack and destroyed all asteroids.
                    stack.append(asteroid)
        return(stack)

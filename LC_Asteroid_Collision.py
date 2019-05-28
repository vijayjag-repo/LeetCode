class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        i = 0
        while(i<len(asteroids)-1):
            if(asteroids[i+1]<0 and asteroids[i]>abs(asteroids[i+1])):
                asteroids.pop(i+1)
            elif(asteroids[i+1]<0 and asteroids[i]>0 and abs(asteroids[i+1])>asteroids[i]):
                asteroids.pop(i)
                if(i>0):
                    i-=1
            elif(asteroids[i+1]<0 and asteroids[i]>0 and abs(asteroids[i+1])==asteroids[i]):
                asteroids.pop(i+1)
                asteroids.pop(i)
                if(i>0):
                    i-=1
            else:
                i+=1
                
            if(len(asteroids)==1):
                break
        return(asteroids)
        

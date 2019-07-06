# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cand = 0
        #First, we find a canditate and we make sure he doesnt know anyone after him.
        for i in range(n):
            if(knows(cand,i)):
                cand = i
                
        #Then, we make sure that this candidate does not know anyone before him        
        for i in range(0,cand):
            if knows(cand,i):
                return(-1)
                
        #Then, we make sure that all the people know this candidate. 
        for i in range(n):
            if not knows(i,cand):
                return(-1)
                
        #We've found a celebrity. Yay!
        return(cand)
                

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        current = 0
        start = 0
        for i in range(len(gas)):
            total+= gas[i] - cost[i]
            current+= gas[i] - cost[i]
            if(current<0):
                start = i+1
                current = 0
        
        if(total>=0):
            return(start)
        else:
            return(-1)

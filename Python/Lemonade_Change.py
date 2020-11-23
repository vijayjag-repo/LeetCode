class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0 
        twenty = 0
        sums = 0
        change = 0
        for i in range(len(bills)):
            if(bills[i]==5):
                sums+=5
                five+=1
            elif(bills[i]==10):
                change = 5
                if(five>=1):
                    sums = sums - change
                    five-=1
                else:
                    return(False)
                sums+=10
                ten+=1
            elif(bills[i]==20):
                change = 15
                if(ten>=1 and five>=1):
                    sums = sums - change
                    ten-=1
                    five-=1
                elif(five>=3):
                    sums = sums - change
                    five-=3
                else:
                    return(False)
                sums+=20
                twenty+=1
        return(True)
        
                        
   

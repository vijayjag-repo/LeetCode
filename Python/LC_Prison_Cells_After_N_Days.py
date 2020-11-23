class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
       
        """
        if not cells:
            return([])
            
        while(N>0):
            ans = []
            ans.append(0)
            for i in range(1,len(cells)-1):
                if(cells[i-1]==cells[i+1]):
                    ans.append(1)
                else:
                    ans.append(0)
            ans.append(0)
            cells = ans
            N = (N-1)%14
        return(ans)
        
        
            

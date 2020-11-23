class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        
        Insert into appropriate indexes until you reach the end. 
        Once you reach numRows, reverse the order of insertion until you reach 0.
        if numRows = 3, 0,1,2,1,0,1,2,1,0,1,2,1,0 ...... Return the 0's first, 1's next and 2's after that. 
        """
        if numRows==1 or numRows>=len(s):
            return s
            
        ans = ['']*numRows
        
        index,step = 0,1
        
        for val in s:
            ans[index]+=val
            if(index==0):
                step = 1
            if(index==numRows-1):
                step = -1
            index+=step
        
        return("".join(ans))

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        
        Approach:
        
        Beautiful solution.
        Initialize walker and runner to 0.
        Get the count of the occurences of any particular element. 
        Update the walker location to this count. If the count exceeds 9, you need to assign multiple places which means that,
        you've to iterate through the str(count).
        
        Key Idea:
        You use walker to get back to the indexes and replace them with the respective counts. 
        You use runner to run through the characters.
        At the end, you'll have walker at the last modified position and you return that+1 to give the length.
        """
        slow,fast = 0,0
        
        while(fast<len(chars)):
            chars[slow] = chars[fast]
            count = 1
            
            while(fast+1<len(chars) and chars[fast]==chars[fast+1]):
                fast+=1
                count+=1
            
            if(count>1):
                for c in str(count):
                    chars[slow+1] = str(c)
                    slow+=1
            
            fast+=1
            slow+=1
        return(slow)
        

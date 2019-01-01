class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        Input: [1,2,3]
        Output: [1,2,4]
        
        Input: [9,9]
        Output: [1,0,0]
        
        """
        rand = []
        news = []
        for i in digits:
            rand.append(str(i))
        new = ''.join(rand)
        new = int(new)
        new+=1
        new = str(new)
        nums = [new[i:i+1] for i in range(0, len(new), 1)]
        for i in nums:
            news.append(int(i))
        return(news) 

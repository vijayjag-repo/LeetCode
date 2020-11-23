# Approach:
# First, reverse the entire string. For example.
# string = ['t','h','e',' ','w','o','r','d'] will be changed into ['d','r','o','w',' ','e','h','t']
# Now, whenever we see a space, we reverse the previous portions. We take note of the index after the space.
# Pass this index to reverse()

class Solution(object):
    def reverse(self,s,start,end):
        while(start<end):
            s[start],s[end] = s[end],s[start]
            start+=1
            end-=1
            
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverse(s,0,len(s)-1)
        
        beg = 0
        for i in range(len(s)):
            if(s[i]==' '):
                self.reverse(s,beg,i-1)
                beg = i+1
            if(i==len(s)-1):
                self.reverse(s,beg,i)
        
        

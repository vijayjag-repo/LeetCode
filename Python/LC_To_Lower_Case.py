class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new = ""
        for i in str:
            if(ord(i)>=65 and ord(i)<=90):
                new+=chr(ord(i)+32)
            else:
                new+=chr(ord(i))
        
        return(new)

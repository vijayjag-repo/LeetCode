class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        Approach:
        First, split the string and store the individual words in a list.
        Then, loop from the last element in the list to the first and add them to a string. 
        After adding the current element, add a space to the string. Keep doing this for all elements. 
        At the end, remove the last space and return the string.
        """
        word = s.split()
        new = ""
        for i in range(len(word)-1,-1,-1):
            new+= word[i] + ' '
        return(new[:-1])
        
        

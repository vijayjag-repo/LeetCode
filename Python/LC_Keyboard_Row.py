class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = set("qwertyuiop")
        row_2 = set("asdfghjkl")
        row_3 = set("zxcvbnm")
        ans = []
        
        for i in words:
            word = set(i.lower())
            if(word<=row_1 or word<=row_2 or word<=row_3):
                ans.append(i)
        
        return(ans)
        

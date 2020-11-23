
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        
        Incomplete. Doesnt work for one case. Able to solve this case with separate code. 
        "a, a, a, a, b,b,b,c, c"
        ["a"]
        """
        new = []
        word = ""
        paragraph = paragraph.lower().split()
        for i in paragraph:
            new.append(i.strip("!,."))
        
        count = collections.Counter(new)
        maximum = 0
        for i in count:
            if(count[i]>maximum and i not in banned):
                maximum = count[i]
                word = i
        return(word)
        
                
        
        
        
        
            
        

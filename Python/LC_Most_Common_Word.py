class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        best = 0
        ans = ""
        paragraph = paragraph.lower()
        str = ",.!@#$%^&*()~`?><:;'[]{}-+_"
        for i in str:
            if(i in paragraph):
                paragraph = paragraph.replace(i,' ')
        line = paragraph.split()
        count = collections.Counter(line)
        for i in count:
            if(i not in banned and count[i]>best):
                ans = i
                best = count[i]
        
        return(ans)
                
      
        

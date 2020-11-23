class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return(True)
        ransom = collections.Counter(ransomNote)
        mag = collections.Counter(magazine)
        
        for i in ransom:
            if(ransom[i]>mag[i]):
                return(False)
        return(True)

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if not logs:
            return []
        
        digits = []
        letters = []
        
        for log in logs:
            if(log.split()[1].isdigit()):
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key = lambda x: (x.split()[1:],x.split()[0]))
        return letters+digits
        

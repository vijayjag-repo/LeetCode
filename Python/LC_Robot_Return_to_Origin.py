class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count = collections.Counter(moves)
        if(count['U']==count['D'] and count['L']==count['R']):
            return(True)
        return(False)
                

import operator
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return("")
        ans = ""
        count = collections.Counter(s)
        
        for (key,val) in sorted(count.items(),key=operator.itemgetter(1),reverse=True):
            ans+=key*val
        return(ans)
        

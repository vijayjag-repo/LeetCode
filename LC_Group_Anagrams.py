class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if(len(strs)==1):
            return([strs])
        d = dict()
        for i in strs:
            new = "".join(sorted(i))
            if new in d:
                d[new]+= [i]
            else:
                d[new] = [i]
        return(d.values())
            
        
        

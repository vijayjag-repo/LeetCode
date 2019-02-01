class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str                   
        """
        new = ""
        if(len(strs)==0):
            return("".join(strs))
        if(len(strs)==1):
            return(strs[0])
        else:
            a = zip(*strs)
            for i in a:
                count = 0
                for j in range(1,len(i)):
                    if(a.index(i)==len(a)-1 and len(a)!=1 and new==""):
                        return("")
                    if(i[j-1]==i[j]):
                        count+=1
                    else:
                        return(new)
                if(count==len(i)-1):
                    new = new + i[j]
            return(new)
            
                
                
                

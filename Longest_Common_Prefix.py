class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Input: ["flower","flow","flight"]
        Output: "fl"
        
        Input: ["aca","cba"] 
        Expected: ""                    
        """
        new = ""
        if(len(strs)==0):
            return("".join(strs))
        if(len(strs)==1):
            for i in strs:
                if(i.isalpha()):
                    return(i)
                return(strs.pop())

        else:
            a = zip(*strs)
            print(a)
            for i in a:
                count = 0
                for j in range(1,len(i)):
                    if(a.index(i)==len(a)-1 and len(a)!=1 and new==""):
                        return("")
                    if(i[j-1]==i[j]):
                        count+=1
                if(count==len(i)-1):
                    new = new + i[j]
            return(new)
                
                
                

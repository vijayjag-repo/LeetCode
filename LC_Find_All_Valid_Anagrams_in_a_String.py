class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        
        Approach:
        Sliding window
        """
        if(len(s)==0 or len(p)==0 or len(p)>len(s)):
            return([])

        count_p = collections.Counter(p)
        count = collections.Counter()
        
        ans = []
        x = 1
        for i in range(len(p)):
            if(s[i] not in count):
                count[s[i]] = 1
            else:
                count[s[i]]+=1
                
        j = len(p)
        while(j<len(s)):
            if(count==count_p):
                ans.append(x-1)
            if(count[s[x-1]]==1):
                del count[s[x-1]]
            else:
                count[s[x-1]]-=1
            count[s[j]]+=1
            j+=1
            x+=1
        if(count==count_p):
            ans.append(x-1)
        return(ans)
        

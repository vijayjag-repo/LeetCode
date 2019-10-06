class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        Approach:
        
        If lesser than next, subtract else add.
        Simple approach.
        """
        if not s:
            return 0
        
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        
        for i in range(len(s)-1):
            if(d[s[i]]<d[s[i+1]]):
                ans-=d[s[i]]
            else:
                ans+=d[s[i]]
            
        return ans+d[s[-1]]
        

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sums = 0
        d = dict()
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        for i in range(1,len(s)):
            if(s[i-1]=='I' and (s[i]=='V' or s[i]=='X')):
                sums+= d[s[i]]-d[s[i-1]]
                d[s[i]] = 0

            elif(s[i-1]=='X' and (s[i]=='L' or s[i]=='C')):
                sums+= d[s[i]]-d[s[i-1]]
                d[s[i]] = 0
                
            elif(s[i-1]=='C' and (s[i]=='D' or s[i]=='M')):
                sums+= d[s[i]]-d[s[i-1]]
                d[s[i]] = 0
                print(sums)
            else:
                sums+= d[s[i-1]]

        sums+= d[s[len(s)-1]]
        return(sums)
        

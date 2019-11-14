class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        Approach:
        
        Simple idea is to traverse from the end and check if curr<prev.
        If curr<prev, then we need to subtract curr from the ans.
        Example: IV => you add V to ans since prev = 0 and V>prev.
        Then you subtract I from ans because I<prev where prev = V.
        Ans = 4.
        
        Easy approach.
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        prev = 0
        
        for i in range(len(s)-1,-1,-1):
            curr = d[s[i]]
            if(curr<prev):
                ans -= curr
            else:
                ans += curr
            prev = d[s[i]]
        
        return ans
            

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
        

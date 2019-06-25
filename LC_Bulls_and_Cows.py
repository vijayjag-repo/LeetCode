class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        how many digits match in digit and position:     bulls(A)
        how many digits match in digit but not position: cows(B)
        """
        count_s = dict()
        count_g = dict()
        same = 0
        ans = ""
        r = 0
        
        for i in range(len(secret)):
            if(secret[i]==guess[i]):
                same+=1
            else:
                if secret[i] not in count_s:
                    count_s[secret[i]] = 1
                else:
                    count_s[secret[i]]+=1
                if guess[i] not in count_g:
                    count_g[guess[i]] = 1
                else:
                    count_g[guess[i]]+=1
        
        for i in count_s:
            if i in count_g:
                r+=min(count_s[i],count_g[i])
        
        
        ans = str(same)+"A"+str(r)+"B"
        return(ans)
        

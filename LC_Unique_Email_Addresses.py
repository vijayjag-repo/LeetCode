class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        
        Approach:
        
        Split into local and domain.
        Process accordingly
        """
        new = set()
        for email in emails:
            local,domain = email.split('@')
            if('+' in local):
                local = local[:local.index('+')]
            if('.' in local):
                local = local.replace('.','')
            new.add(local+'@'+domain)
        return(len(new))
                
            

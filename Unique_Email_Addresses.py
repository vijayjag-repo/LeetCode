class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        new = set()
        for i in emails:
            local,domain = i.split('@')
            if '+' in local:
                local = local[:local.index('+')]
                local = local.replace('.','')
                new.add(local + '@' + domain)
        return(len(new))
                
                
            
            
            

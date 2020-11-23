class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        ans = i = 0
        count = collections.Counter()
        for index, val in enumerate(tree):
            count[val]+= 1
            while(len(count)>2):
                count[tree[i]]-=1
                if(count[tree[i]]==0):
                    del count[tree[i]]
                i+=1
            ans = max(ans,index-i+1)
        return(ans)
                

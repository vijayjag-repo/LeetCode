class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        
        def dfs(candidates,target,index,path,res):
            if(target<0):
                return
            if(target==0):
                res.append(path)
                return
            
            for i in range(index,len(candidates)):
                if(candidates[i]>target):
                    break
                dfs(candidates,target-candidates[i],i,path+[candidates[i]],res)
            
        dfs(candidates,target,0,[],res)
        return(res)

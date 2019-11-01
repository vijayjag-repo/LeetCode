class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        
        Approach:
        
        Standard Backtracking. 
        Key idea is that, we can use the same number multiple times. Inside the for loop while calling dfs(),
        we pass the index as i instead of i+1. i -> gaurantees that the same element is used multiple times whereas i+1 will ensure that,
        only the unique elements add up to a particular sum.
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

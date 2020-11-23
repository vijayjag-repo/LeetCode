class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        
        Approach:
        
        Leetcode discuss solution
        
        Given, arr is the inorder traversal of leaf nodes in a tree.
        First, choose the minimum element to start with.
        Since, its inorder traversal of leaf nodes, you have to choose a node present on either side of the minimum,
        to assign as fellow leaf node of a sub-tree.
        Now, you multiply the minimum along with the minimum of the neighboring nodes to add to the sum.
        Then you pop out the minimum using the index.
        Now,
        If your minimum is at index 0, then you only can choose index 1 as partner(fellow leaf node of same subtree)
        If your minimum is at index len(arr)-1, you can only choose len(arr)-2.
        
        This is the basic idea behind this solution
        """
        ans = 0
        while(len(arr)>1):
            min_idx = arr.index(min(arr))
            if(0<min_idx<len(arr)-1):
                ans+= min(arr[min_idx-1],arr[min_idx+1])*arr[min_idx]
            else:
                ans+= arr[1 if min_idx==0 else min_idx-1]*arr[min_idx]
        
            arr.pop(min_idx)
        return(ans)
        
        

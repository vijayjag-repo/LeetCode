# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        
        Approach:
        
        Instead of storing the entire tree into a list and then checking for two sum, we can process it just like a list.
        If root.val not there in dict, store its counter value. 
        Recursively go left and right. 
        
        """
        d = dict()
     
        def helper(root,k):
            if not root:
                return
            else:
                if(root.val in d):
                    return(True)
                d[k-root.val] = 1
                
                if(True==helper(root.left,k)):
                    return(True)
                if(True==helper(root.right,k)):
                    return(True)
                
        return(helper(root,k))
        
                

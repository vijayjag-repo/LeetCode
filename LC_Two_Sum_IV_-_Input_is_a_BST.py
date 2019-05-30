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
        """
        new = []
        def helper(root):
            if(root!=None):
                helper(root.left)
                new.append(root.val)
                helper(root.right)
                
        helper(root)
        i = 0
        j = len(new)-1
        sums = 0
        while(i<j):
            sums = new[i]+new[j]
            if(sums==k):
                return(True)
            elif(sums>k):
                j-=1
            elif(sums<k):
                i+=1
        
        return(False)
        
            
        

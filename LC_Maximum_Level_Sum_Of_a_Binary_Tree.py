# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(None)
        level = [root]
        ans = []
        
        while(level):
            current = []
            child = []
            for node in level:
                current.append(node.val)
                if(node.left):
                    child.append(node.left)
                if(node.right):
                    child.append(node.right)
            
            ans.append(current)
            level = child
        
        max_val = 0
        ind = 0
        for row in ans:
            if(sum(row)>max_val):
                max_val = sum(row)
                ind = ans.index(row)
        return(ind+1)
        
        
                

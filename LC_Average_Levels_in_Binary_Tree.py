# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = []
        avg = []
        if not root:
            return(levels)
        
        def helper(root,level):
            if(len(levels)==level):
                levels.append([])
            
            levels[level].append(root.val)
            if(root.left):
                helper(root.left,level+1)
            if(root.right):
                helper(root.right,level+1)
                
        helper(root,0)
        for i in levels:
            avg.append(float(sum(i))/len(i))
        
        return(avg)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#       Two Solutions, same as level order traversal.
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
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
if not root:
            return(None)
        
        ans = []
        level = [root]
        while(level):
            current = []
            child = []
            for node in level:
                current.append(node.val)
                if(node.left):
                    child.append(node.left)
                if(node.right):
                    child.append(node.right)
            
            ans.append(float(sum(current))/len(current)
            level = child
        
        return(ans)

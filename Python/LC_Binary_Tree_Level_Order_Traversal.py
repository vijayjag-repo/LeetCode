# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#   Two solutions to this problem
#   Solution 1:
#       if the length of the list is equal to the level, then create a new [] and append this value and store it at index=level
#       Example: If root.val==3, level=0, len(levels)==0, then, levels=[[3]]
#       Simlarly, if root.val has a left and right, then their level is 1 greater than root's level.
#       Therefore, level=1,len(levels)=1 (since root was added), root.left.val is added at index=1=level
#       Since this is a recursive process, all left node values are added to their respective indexes.

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
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
        return(levels)
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - 
#   Solution 2:
#       level = [root] ----> initialise level with root
#       while(level exists):
#       current level = [], child_level = []
#       for each item in level:
#           append its value to the current level. If the current item has a child, append it to the child level.
#       append all values in the current level to the ans.
#       now, since this level is done, we proceed to the next level which is the child level.
#       This can be done by setting level = child and the same process continues.

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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
            
            ans.append(current)
            level = child
        
        return(ans)

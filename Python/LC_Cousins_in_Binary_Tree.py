# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        Approach:
        
        Same as level order traversal except that, whenever you see x or y, you store its level and parent in lhs and rhs.
        lhs will store [level of x,parent of x]
        rhs will store [level of y,parent of y]
        when you compare these two, if levels are the same and parents are different, you return True
        else, return False
        """
        if not root:
            return(None)
        lhs = []
        rhs = []
        lev = 1
        ans = []
        level = [root]
        while(level):
            current = []
            child = []
            for node in level:
                current.append(node.val)
                if(node.left):
                    if(node.left.val==x):
                        lhs.append(lev)
                        lhs.append(node.val)
                    if(node.left.val==y):
                        rhs.append(lev)
                        rhs.append(node.val)
                    child.append(node.left)
                if(node.right):
                    if(node.right.val==x):
                        lhs.append(lev)
                        lhs.append(node.val)
                    if(node.right.val==y):
                        rhs.append(lev)
                        rhs.append(node.val)
                    child.append(node.right)
            
            ans.append(current)
            lev+=1
            level = child
            if(lhs and rhs and lhs[0]==rhs[0] and lhs[1]!=rhs[1]):
                return(True)
        
        return(False)
        

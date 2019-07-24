# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        
        Approach:
        
        As and when you go along a path, pass on difference in sum left.
        If we reach a leaf node, we check if the difference is equal to the leaf node val. 
        """
        def helper(root,sum):
            if not root:
                return(False)
            elif(not root.left and not root.right):
                return(sum==root.val)
            else:
                return(self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val))
        
        return(helper(root,sum))
    
# DFS - Stack based approach
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
     
        """
        if not root:
            return(False)
        stack = [(root,[root.val])]
        while(stack):
            curr,total = stack.pop()
            if(not curr.left and not curr.right and sum(total)==sums):
                return(True)
            if(curr.left):
                stack.append((curr.left,total+[curr.left.val]))
            if(curr.right):
                stack.append((curr.right,total+[curr.right.val]))
        return(False)

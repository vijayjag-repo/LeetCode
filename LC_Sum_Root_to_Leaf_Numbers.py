# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Recursive solution 
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        self.total = 0
        def helper(root,sums):
            if not root:
                return
            if not root.left and not root.right:
                sums+=root.val
                self.total+=sums
                return
            
            sums+=root.val
            if(root.left):
                helper(root.left,sums*10)
            if(root.right):
                helper(root.right,sums*10)
        
        helper(root,0)
        return(self.total)
                
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        Approach:
        
        DFS Stack
        """
        if not root:
            return(0)
        ans = []
        stack = [(root,str(root.val))]
        while(stack):
            curr,total = stack.pop()
            if(not curr.left and not curr.right):
                ans.append(int(total))
            if(curr.left):
                stack.append((curr.left,total+str(curr.left.val)))
            if(curr.right):
                stack.append((curr.right,total+str(curr.right.val)))
    
        return(sum(ans))

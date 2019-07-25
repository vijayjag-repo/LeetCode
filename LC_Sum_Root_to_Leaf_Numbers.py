# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

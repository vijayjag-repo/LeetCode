# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        
        Same as Level Order Traversal. Just return the last element from each level.
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
        
        return([i[-1] for i in ans])
            
        

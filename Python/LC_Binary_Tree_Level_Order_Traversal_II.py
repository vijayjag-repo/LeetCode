# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        Approach:
            Same as level order traversal but just that you insert from the end. 
        """
        if not root:
            return(None)
        k = 1
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
            ans.insert(-k,current)
            k+=1
            level = child
        
        return(ans)

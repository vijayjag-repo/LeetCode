# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        Approach:
        Same as level order traversal but you have a flag to reverse alternate entries. 
        """
        if not root:
            return(None)
        
        flag = 0
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
            
            if(flag==1):
                ans.append(current[::-1])
                flag = 0
            else:
                ans.append(current)
                flag = 1
            
            level = child
        
        return(ans)

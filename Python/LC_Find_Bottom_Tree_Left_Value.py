# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Approach:
        
        Do level order traversal from the right. Last element in the queue is the left most element.
        """
        queue = [root]
        ans = 0
        
        while(queue):
            node = queue.pop(0)
            ans = node.val
            
            if(node.right):
                queue.append(node.right)
            if(node.left):
                queue.append(node.left)
            
        return(ans)

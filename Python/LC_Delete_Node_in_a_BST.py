# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        Approach:
        
        Uses the concept of predecessor. You can replace with predecessor or successor. Here, I've replaced with predecessor.
        1) First, you navigate through the tree to find the key.
        2) Once you find it, you check if it has a left,right.
        3) If it doesn't have left, you just return the right.
        4) If it has both left and right, you can either return the predecessor which is present in the left.
        Or, the successor which is present in the right.(Both are accepted in this problem).
        5) So, you traverse the left part of the key to find the predecessor.
          For predecessor, you move left once and keep going right.
          For sucessor, you move right and keep going left.
          So, you find the predecessor using the above and replace it with the key.
        6) Now, our key is deleted but the predecessor remains. So, you delete this.(recursive call)
        
        """
        if not root:
            return(None)
        elif(root.val<key):
            root.right = self.deleteNode(root.right,key)
        elif(root.val>key):
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return(root.right)
            else:
                temp = root.left
                while(temp.right):
                    temp = temp.right
            
                root.val = temp.val
                root.left = self.deleteNode(root.left,temp.val)
        return(root)
        

# Iterative as well Recursive solution added

# Iterative Approach
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return(None)
        
        new = root
        while(new):
            if(new.val<val):
                if(new.right):
                    new = new.right
                else:
                    new.right = TreeNode(val)
                    break
            if(new.val>val):
                if(new.left):
                    new = new.left
                else:
                    new.left = TreeNode(val)
                    break
        
        return(root)

# Recursive Approach
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return(None)
        
        def helper(root,val):
            if not root:
                return(None)
            else:
                if(root.val<val):
                    if(root.right):
                        helper(root.right,val)
                    else:
                        root.right = TreeNode(val)
                elif(root.val>val):
                    if(root.left):
                        helper(root.left,val)
                    else:
                        root.left = TreeNode(val)
            
            return(root)
        return(helper(root,val))

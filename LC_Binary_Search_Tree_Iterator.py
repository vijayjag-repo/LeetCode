# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#   Solution using Stack: 
#   This is a beautiful way to do. Because, you are keeping only h(height of stack) elements on an average.
#   Notice that the insert into the stack is always at index 0.

#   Other way to do this without the stack is to perform inorder traversal but you are keeping all the elements,
#   so it defeats the purpose. However, if you can store all elements, this is also an option.

def helper(stack,root):
    while(root!=None):
        stack.insert(0,root)
        root = root.left
    
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        helper(self.stack,root)
            
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        root = self.stack.pop(0)
        helper(self.stack,root.right)
        return(root.val)
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if(len(self.stack)!=0):
            return(True)
        return(False)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

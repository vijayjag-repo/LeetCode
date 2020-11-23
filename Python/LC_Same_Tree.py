# Recursive, DFS, BFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Approach:
# All approaches are straightforward.
# Notice the use of pop() in DFS and BFS. 
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if(not p and not q):
            return(True)
        else:
            if(p and q):
                return(p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
            else:
                return(False)
        
# DFS Stack
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p,q)]
        while(stack):
            node1,node2 = stack.pop()
            if(not node1 and not node2):
                continue
            elif None in [node1,node2]:
                return(False)
            elif(node1.val!=node2.val):
                return(False)
            else:
                stack.append((node1.left,node2.left))
                stack.append((node1.right,node2.right))
        return(True)
    
# BFS Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p,q)]
        while(stack):
            node1,node2 = stack.pop(0)
            if(not node1 and not node2):
                continue
            elif None in [node1,node2]:
                return(False)
            elif(node1.val!=node2.val):
                return(False)
            else:
                stack.append((node1.left,node2.left))
                stack.append((node1.right,node2.right))
        return(True)
            

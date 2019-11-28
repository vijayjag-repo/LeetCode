# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from hashlib import sha256
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        
        Approach:
        
        Merkle Hashing.
        Time complexity: size(s)+size(t)
        """
        def _hash(x):
            val = sha256()
            val.update(x)
            return val.hexdigest()
        
        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = _hash(m_left+str(node.val)+m_right)
            return node.merkle
        
        merkle(s)
        merkle(t)
        
        def dfs(s):
            if not s:
                return False
            else:
                return s.merkle==t.merkle or dfs(s.left) or dfs(s.right)
        return dfs(s)
  
  
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        
        Time Complexity = size(s)*size(t)
        """
        def match(t1,t2):
            if(t1 is None and t2 is None):
                return True
            elif(t1 is None or t2 is None):
                return False
            else:
                return t1.val==t2.val and match(t1.left,t2.left) and match(t1.right,t2.right)
            
        if not s:
            return False
        elif(match(s,t)):
            return True
        else:
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        
        Approach:
        Pretty intuitive method. Have a stack and keep appending the node and the corresponding sum till then.
        If right exists, go right recursively and keep going. Along the way, add the sums and keep checking.
        Finally, return the ans.
        
        """
        if not root:
            return []
        ans = []
        stack = [(root, [root.val])]
        while(stack):
            curr, total = stack.pop()
            if(not curr.left and not curr.right and sum(total)==sums):
                ans.append(total)
            if(curr.right):
                stack.append((curr.right, total+[curr.right.val]))
            if(curr.left):
                stack.append((curr.left, total+[curr.left.val]))
        return(ans)

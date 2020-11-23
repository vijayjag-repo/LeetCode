# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        
        Approach:
        
        Find the max element index. That's the root node.
        Recursively compute left and right by passing the nums list accordingly.
        Return the node.
        """
        if not nums:
            return(None)
        max_index = nums.index(max(nums))
        def helper(nums):
            if not nums:
                return
            max_index = nums.index(max(nums))
            node = TreeNode(nums[max_index])
            node.left = helper(nums[:max_index])
            node.right = helper(nums[max_index+1:])
            return(node)
        
        return(helper(nums))
    
        
        

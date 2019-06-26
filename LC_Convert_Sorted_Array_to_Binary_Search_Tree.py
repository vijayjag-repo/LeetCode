# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(low,high):
            if(low>high):
                return(None)
            mid = (low+high)//2
            root = TreeNode(nums[mid])
            root.left = helper(low,mid-1)
            root.right = helper(mid+1,high)
            return(root)
        
        return helper(0,len(nums)-1)
        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        array = []
        def dfs(node,x,y):
            if not node:
                return
            array.append((x,y,node.val))
            dfs(node.left,x-1,y+1)
            dfs(node.right,x+1,y+1)
        dfs(root,0,0)
    
        array = sorted(array,key = lambda x: [x[0],x[1],x[2]])
    
        ans.append([array[0][2]])
        for i in range(1,len(array)):
            if(array[i][0]==array[i-1][0]):
                ans[-1].append(array[i][2])
            else:
                ans.append([array[i][2]])
        
        return ans
        

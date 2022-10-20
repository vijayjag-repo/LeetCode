# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Approach 1:

        Pretty simple. Consider the root to be at position 0.
        Every left that you take while traversing, decrement the position by -1
        Similarly, every right that you take while traversing, increment the position by +1.
        For each position, maintain a list and continually keep appending nodes according to their positions.
        Finally return the list of all positions in sorted manner

        Time complexity: O(n logn)
        Space complexity: O(n)
        """
        if not root:
            return []

        q = collections.deque([(root, 0)])
        d = collections.defaultdict(list)

        while q:
            node, val = q.popleft()
            if node:
                d[val].append(node.val)
                q.append((node.left, val - 1))
                q.append((node.right, val + 1))

        return [d[key] for key in sorted(d)]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Approach 2:

        Same as approach 1 but except that instead of sorting the keys in the dict based on their val,
        we instead using a min, max range to return the corresponding List

        Min_val = position of the node farthest on the left
        Max_val = position of the node farthest on the right

        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return []

        q = collections.deque([(root, 0)])
        d = collections.defaultdict(list)
        min_val = 0
        max_val = 0

        while q:
            node, val = q.popleft()
            if node:
                d[val].append(node.val)
                min_val = min(min_val, val)
                max_val = max(max_val, val)
                q.append((node.left, val - 1))
                q.append((node.right, val + 1))

        return [d[key] for key in range(min_val, max_val + 1)]

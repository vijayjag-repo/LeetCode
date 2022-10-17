# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Pretty Straightforward approach

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def depthSum(self, nestedList):

        def dfs(nestedList, depth):
            total = 0
            for item in nestedList:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)

# Similar approach but handles each type of NestedInteger separately
class Solution:
    def depthSum(self, nestedList):
        self.ans = 0

        def dfs(item, depth):
            if (item.isInteger()):
                self.ans += item.getInteger() * depth
            elif (item.getInteger() == None):
                for ele in item.getList():
                    dfs(ele, depth + 1)
            else:
                for ele in item:
                    dfs(ele, depth + 1)

        for item in nestedList:
            dfs(item, 1)

        return self.ans

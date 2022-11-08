class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str

        Typical stack question based on comparing the current element and the top of the stack

        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = []

        for i in range(len(s)):
            if (len(stack) > 0):
                if (s[i] != stack[-1]):
                    if (s[i].lower() == stack[-1].lower()):
                        stack.pop()
                        continue
            stack.append(s[i])

        return "".join(stack)

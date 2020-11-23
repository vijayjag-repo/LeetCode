class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        temp = s.split()
        return " ".join(temp[::-1])

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int

        Approach:
        Basic idea is that in a palindrome, each character if present twice if length=even and similarly for odd except one char.
        So, we just add the count of the character and if its odd, you add the count-1.
        Finally, we add +1 if some character is present odd number of times because atmost one character can be present odd number of times.

        """
        d = collections.Counter(s)
        ans = 0
        odd_flag = False

        for ele in d:
            if (d[ele] % 2 == 0):
                ans += d[ele]
            elif (d[ele] % 2 != 0):
                odd_flag = True
                ans += d[ele]-1

        if odd_flag:
            ans += 1

        return ans

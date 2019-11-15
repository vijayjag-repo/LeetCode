class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        
        Approach:
        
        For each value present, we'll see which val divided the given num. If the val divides the given number,
        it has to be added to the answer(the same value can divide the number multiple times=>multiple occurences).
        Then since the number has been divided, the number changes to the remainder after division.
        This process continues.
        """
        if not num:
            return ""
            
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        ans = ""
        for i,val in enumerate(values):
            ans += (num/val) * numerals[i]
            num %= val
        
        return ans

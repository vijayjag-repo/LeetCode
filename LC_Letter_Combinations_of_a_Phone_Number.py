class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        output = []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        def backtrack(combination, digits):
            if(len(digits)==0):
                output.append(combination)
            else:
                for letter in phone[digits[0]]:
                    backtrack(combination+letter,digits[1:])
        
        if(digits):
            backtrack("",digits)
        return(output)

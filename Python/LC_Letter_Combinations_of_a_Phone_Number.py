class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        Approach:
        
        At every single step you have to take a decision. A decision tree would be the best approach.
        First, you choose '2' -> you choose 'a' and then you go on to '3' -> choose 'd'.
        Then you exhaust all the possible choices in '3' because '3' is the last digit present.
        i.e: 'ad','ae','af' -> 'b' -> 'bd','be','bf' -> 'c' and so on.
        Pretty intuitive if you draw the tree
        
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

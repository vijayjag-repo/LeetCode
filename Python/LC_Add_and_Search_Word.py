class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isword = False
    
class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.isword = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.root
        self.ans = False
        self.dfs(current,word)
        return(self.ans)
    
    def dfs(self, current, word):
        if not word:
            if current.isword:
                self.ans = True
            return 
        if word[0] == ".":
            for n in current.children.values():
                self.dfs(n, word[1:])
        else:
            current = current.children.get(word[0])
            if not current:
                return 
            self.dfs(current, word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

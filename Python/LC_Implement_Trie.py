# Just learnt it today. Tushar Roy video for explanation. Pretty simple to understand. 

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if(current==None):
                return(False)
        return(current.is_word)
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if(current==None):
                return(False)
        return(True)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

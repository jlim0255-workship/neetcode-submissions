class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root

        # go through every char
        for c in word:
            # if we not yet seen this char
            if c not in cur.children:
                # create a new node for this char
                cur.children[c] = TrieNode()

            # else, move to this node
            cur = cur.children[c]

        # mark end of word true
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return True
        
        
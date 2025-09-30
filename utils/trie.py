class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.isEndOfWord = False

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str):
        curr = self.root

        for c in word:
            if not c:
                continue
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = Trie.Node()
                curr = curr.children[c]

        curr.isEndOfWord = True

    def get_common_prefix(self) -> str:
        curr = self.root
        prefix = ""

        while not curr.isEndOfWord and len(curr.children) == 1:
            char = list(curr.children.keys())[0]
            prefix += char
            curr = curr.children[char]

        return prefix

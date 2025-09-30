class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.isEndOfWord = False

        def __len__(self):
            return len(self.children)

        def __contains__(self, s: str):
            return s in self.children

        def __getitem__(self, s: str):
            return self.children[s]

        def __setitem__(self, key: str, value):
            self.children[key] = value

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str):
        curr = self.root

        for c in word:
            if not c:
                continue
            if c in curr:
                curr = curr[c]
            else:
                curr[c] = Trie.Node()
                curr = curr[c]

        curr.isEndOfWord = True

    def get_common_prefix(self) -> str:
        curr = self.root
        prefix = ""

        while not curr.isEndOfWord and len(curr) == 1:
            char = list(curr.children.keys())[0]
            prefix += char
            curr = curr[char]

        return prefix

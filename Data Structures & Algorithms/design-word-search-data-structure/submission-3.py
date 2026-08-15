class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def __repr__(self):
        return f"TrieNode(is_end={self.is_end},children={list(self.children.keys())})"


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node, i):
            if i == len(word):
                return node.is_end

            c = word[i]

            if c == ".":
                if not node.children:
                    return False
                for n in node.children.values():
                    if dfs(n,i+1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                node = node.children[c]
                return dfs(node,i+1)

        return dfs(node, 0)


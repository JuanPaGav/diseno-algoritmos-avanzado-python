"""Trie: inserción, búsqueda exacta y búsqueda por prefijo."""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_word = True

    def _walk(self, text):
        node = self.root
        for char in text:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        return self._walk(prefix) is not None


def build_suffix_trie(texto):
    trie = Trie()
    for i in range(len(texto)):
        trie.insert(texto[i:])
    return trie


if __name__ == "__main__":
    trie = Trie()
    for palabra in ("casa", "caso", "cama"):
        trie.insert(palabra)
    print(trie.search("casa"), trie.starts_with("cas"))
    print(build_suffix_trie("banana").starts_with("ana"))



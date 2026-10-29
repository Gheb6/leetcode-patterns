"""
Problem: Implement Trie (Prefix Tree)
LeetCode: 208 (https://leetcode.com/problems/implement-trie-prefix-tree/)
NeetCode 150: Implement Trie (Prefix Tree) (https://neetcode.io/problems/implement-prefix-tree)
Difficulty: Medium
Pattern: Tries (Prefix Tree / Hash Map Nodes)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# Alias for LeetCode naming convention
Trie = PrefixTree


if __name__ == "__main__":
    # Test case 1: Example from NeetCode
    prefixTree = PrefixTree()
    prefixTree.insert("dog")
    assert prefixTree.search("dog") is True, "Failed searching 'dog'"
    assert prefixTree.search("do") is False, "Failed searching prefix 'do' before insertion"
    assert prefixTree.startsWith("do") is True, "Failed startsWith 'do'"
    prefixTree.insert("do")
    assert prefixTree.search("do") is True, "Failed searching 'do' after insertion"

    # Test case 2: Example from LeetCode
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True, "Failed searching 'apple'"
    assert trie.search("app") is False, "Failed searching 'app' before insertion"
    assert trie.startsWith("app") is True, "Failed startsWith 'app'"
    trie.insert("app")
    assert trie.search("app") is True, "Failed searching 'app' after insertion"

    # Test case 3: Non-existent prefix and word
    assert trie.search("banana") is False, "Failed on non-existent word"
    assert trie.startsWith("ban") is False, "Failed on non-existent prefix"

    print("All test cases for Implement Trie (Prefix Tree) passed!")

# Implement Trie (Prefix Tree)

- **Source**: LeetCode 208 / NeetCode 150
- **Links**: [LeetCode #208](https://leetcode.com/problems/implement-trie-prefix-tree/) | [NeetCode](https://neetcode.io/problems/implement-prefix-tree)
- **Difficulty**: Medium
- **Pattern**: Tries (Prefix Tree / Hash Map Nodes)

---

## Problem Description
A **trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the `PrefixTree` (or `Trie`) class:
- `PrefixTree()`: Initializes the trie object.
- `void insert(String word)`: Inserts the string `word` into the trie.
- `boolean search(String word)`: Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)`: Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

### Example
```text
Input:
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true
```

### Constraints
- $1 \le \text{word.length}, \text{prefix.length} \le 2000$
- `word` and `prefix` consist only of lowercase English letters.
- At most $3 \times 10^4$ calls in total will be made to `insert`, `search`, and `startsWith`.

---

## Strategy & Approach
A Trie is an $m$-ary tree where each node represents a character. Shared prefixes reuse existing nodes, allowing efficient prefix queries.

### Node Structure (`TrieNode`):
- `children`: A hash map (dictionary) mapping characters to child `TrieNode` instances (`dict[str, TrieNode]`).
- `is_end`: A boolean flag indicating whether a complete word terminates at this node.

### Operations:
1. **`insert(word)`**:
   - Traverse starting from `root`.
   - For each character $c$ in `word`, if $c$ is not in `curr.children`, instantiate a new `TrieNode`.
   - Advance `curr = curr.children[c]`.
   - After processing all characters, set `curr.is_end = True`.
2. **`search(word)`**:
   - Traverse character by character.
   - If any character $c$ is absent from `curr.children`, the word does not exist: return `False`.
   - If the full path exists, return `curr.is_end` (to distinguish full words from partial prefixes).
3. **`startsWith(prefix)`**:
   - Similar to `search`, but does not require `curr.is_end == True`. If all characters in `prefix` exist along the path, return `True`.

---

## Complexity Analysis
- **Time Complexity**:
  - `insert(word)`: $\mathcal{O}(L)$ where $L = \text{len}(word)$.
  - `search(word)`: $\mathcal{O}(L)$ where $L = \text{len}(word)$.
  - `startsWith(prefix)`: $\mathcal{O}(P)$ where $P = \text{len}(prefix)$.
- **Space Complexity**:
  - $\mathcal{O}(N \cdot L)$ in the worst case where $N$ distinct words of average length $L$ with no common prefixes are inserted. Common prefixes compress node allocation.

---

## Edge Cases Considered
- **Word is a prefix of another word** (e.g. searching `"do"` when only `"dog"` was inserted): Correctly returns `False` for `search` and `True` for `startsWith`.
- **Single character words**: Node creation and flag setting execute without edge issues.
- **Querying uninserted prefixes**: Handled immediately by returning `False` upon missing child.

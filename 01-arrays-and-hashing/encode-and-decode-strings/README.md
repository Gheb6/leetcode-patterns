# Encode and Decode Strings

- **Source**: LeetCode 271 / NeetCode 150
- **Links**: [LeetCode #271](https://leetcode.com/problems/encode-and-decode-strings/) | [NeetCode](https://neetcode.io/problems/string-encode-and-decode)
- **Difficulty**: Medium
- **Pattern**: Arrays & Hashing / String

---

## Problem Description
Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network and is decoded back to the original list of strings.

---

## Intuition & Approach
- Use a **length-prefix** encoding format: `<length>#<string>`.
- The delimiter `#` preceded by the word length guarantees that any character inside `<string>` (even `#` itself or special characters) is not misinterpreted as a delimiter.
- In `decode`, find the next `#` delimiter, parse the integer length, extract exactly that many characters, and advance the pointer.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ for both `encode` and `decode`, where $N$ is the total number of characters.
- **Space Complexity**: $\mathcal{O}(N)$ to store the encoded string / decoded list.

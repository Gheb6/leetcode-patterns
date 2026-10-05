# Valid Parentheses

- **Source**: LeetCode 20 / NeetCode 150
- **Links**: [LeetCode #20](https://leetcode.com/problems/valid-parentheses/) | [NeetCode](https://neetcode.io/problems/validate-parentheses)
- **Difficulty**: Easy
- **Pattern**: Stack

---

## Problem Description
Given a string `s` containing `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. Brackets must close in the correct order with matching pairs.

---

## Intuition & Approach
- Iterate through the characters using a **Stack**.
- Push opening brackets (`(`, `[`, `{`) onto the stack.
- For closing brackets, check if the stack is non-empty and the top matches the corresponding open bracket; pop if matched, else return `False`.
- Return `True` if the stack is empty at the end, `False` otherwise.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$
- **Space Complexity**: $\mathcal{O}(n)$

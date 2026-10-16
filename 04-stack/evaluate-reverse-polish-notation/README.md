# Evaluate Reverse Polish Notation

- **Source**: LeetCode 150 / NeetCode 150
- **Links**: [LeetCode #150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [NeetCode](https://neetcode.io/problems/evaluate-reverse-polish-notation)
- **Difficulty**: Medium
- **Pattern**: Stack

---

## Problem Description
You are given an array of strings `tokens` that represents an arithmetic expression in a **Reverse Polish Notation** (postfix notation).

Evaluate the expression. Return an integer that represents the value of the expression.

> **Note**:
> - The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
> - Each operand may be an integer or another expression.
> - The division between two integers always **truncates toward zero** (e.g. `int(a / b)` in Python).
> - There will not be any division by zero.
> - The input represents a valid arithmetic expression in Reverse Polish Notation.
> - The answer and all intermediate calculations can be represented in a 32-bit signed integer.

### Example 1
```text
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Example 2
```text
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### Example 3
```text
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation:
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 22
```

### Constraints
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

---

## Intuition & Approach
In Reverse Polish Notation (RPN), operators follow their operands. This evaluation order maps naturally to a **Last-In, First-Out (LIFO) Stack**:

1. **Stack Initialization**: Maintain an empty stack `my_stack` to hold intermediate evaluation values.
2. **Handling Single Token**: If `len(tokens) == 1`, return `int(tokens[0])` directly.
3. **Iterative Evaluation**:
   - For each `token` in `tokens`:
     - **Operand**: If `token not in operations`, convert it to an integer `int(token)` and push it onto `my_stack`.
     - **Operator**:
       - Pop the top value as the second operand `elem_2 = my_stack.pop()`.
       - Pop the next value as the first operand `elem_1 = my_stack.pop()`.
       - Compute the result based on the operator:
         - `+`: `elem_1 + elem_2`
         - `-`: `elem_1 - elem_2`
         - `*`: `elem_1 * elem_2`
         - `/`: `int(elem_1 / elem_2)` (floating-point division converted to integer in Python ensures truncation towards zero, avoiding floor division `//` which rounds toward negative infinity for negative numbers).
       - Push the computed result back onto `my_stack`.
4. **Final Result**: Once all tokens have been processed, the stack contains exactly one element which is the final answer: `return my_stack[0]`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We process each of the $n$ tokens exactly once. Push and pop operations on the stack take $\mathcal{O}(1)$ time.
- **Space Complexity**: $\mathcal{O}(n)$ — In the worst case (e.g. all operands appear before operators), the stack stores up to $\lceil n / 2 \rceil$ operands simultaneously.

---

## Edge Cases Considered
- **Single element expression**: `tokens = ["42"]` correctly returns `42`.
- **Negative numbers**: Tokens like `"-11"` are handled correctly as negative integers rather than minus operators.
- **Division truncation towards zero**: Expressions with negative division like `6 / -132` evaluate to `0` via `int(elem_1 / elem_2)` instead of `-1` (which Python's integer division `//` would produce).

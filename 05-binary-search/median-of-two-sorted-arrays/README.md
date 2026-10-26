# Median of Two Sorted Arrays

- **Source**: LeetCode 4 / NeetCode 150
- **Links**: [LeetCode #4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [NeetCode](https://neetcode.io/problems/median-of-two-sorted-arrays)
- **Difficulty**: Hard
- **Pattern**: Binary Search (Partition / Two Arrays)

---

## Problem Description
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.

The overall run time complexity should be $\mathcal{O}(\log (m+n))$.

### Example 1
```text
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1, 2, 3] and median is 2.
```

### Example 2
```text
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.50000
Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
```

### Constraints
- $\text{nums1.length} == m$
- $\text{nums2.length} == n$
- $0 \le m \le 1000$
- $0 \le n \le 1000$
- $1 \le m + n \le 2000$
- $-10^6 \le \text{nums1}[i], \text{nums2}[i] \le 10^6$

---

## Intuition & Approach
Instead of merging the two arrays in $\mathcal{O}(m + n)$ time, we use binary search to find the correct partition dividing both arrays into left and right halves of equal length.

1. **Ensure $n \le m$**:
   - Always perform binary search on the shorter array (`nums1`) so the search space is minimized to $[0, n]$, guaranteeing $\mathcal{O}(\log(\min(n, m)))$.

2. **Partition Condition**:
   - Let partition index $i$ in `nums1` and partition index $j = \lfloor(n + m + 1) / 2\rfloor - i$ in `nums2`.
   - The elements immediately surrounding the partitions are:
     - $A_{\text{left}} = \text{nums1}[i-1]$ (or $-\infty$ if $i = 0$)
     - $A_{\text{right}} = \text{nums1}[i]$ (or $+\infty$ if $i = n$)
     - $B_{\text{left}} = \text{nums2}[j-1]$ (or $-\infty$ if $j = 0$)
     - $B_{\text{right}} = \text{nums2}[j]$ (or $+\infty$ if $j = m$)

3. **Binary Search Logic**:
   - If $A_{\text{left}} \le B_{\text{right}}$ and $B_{\text{left}} \le A_{\text{right}}$:
     - The partition is correct!
     - If the combined length $n + m$ is **odd**, the median is $\max(A_{\text{left}}, B_{\text{left}})$.
     - If **even**, the median is $\frac{\max(A_{\text{left}}, B_{\text{left}}) + \min(A_{\text{right}}, B_{\text{right}})}{2}$.
   - Else if $A_{\text{left}} > B_{\text{right}}$:
     - Too many large elements from `nums1` are in the left half; shift the partition left: `right = i - 1`.
   - Else:
     - Partition in `nums1` is too far left; shift it right: `left = i + 1`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log(\min(n, m)))$ — Binary search is performed on the smaller array.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary space; no merged arrays created.

---

## Edge Cases Considered
- **One empty array** (e.g. `nums1 = []`, `nums2 = [1]`): Swapped to place the empty array first; partitions correctly handle boundary conditions with $-\infty$ and $+\infty$.
- **Odd vs. Even total lengths**: Accommodated using the $\lfloor(n + m + 1) / 2\rfloor$ half-size formula.
- **Completely disjoint ranges** (e.g. all elements of `nums1` are larger than `nums2`): Handled safely without index out of bounds.

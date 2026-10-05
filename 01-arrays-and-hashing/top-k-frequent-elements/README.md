# Top K Frequent Elements

- **Source**: LeetCode 347 / NeetCode 150
- **Links**: [LeetCode #347](https://leetcode.com/problems/top-k-frequent-elements/) | [NeetCode](https://neetcode.io/problems/top-k-elements-in-list)
- **Difficulty**: Medium
- **Pattern**: Arrays & Hashing (Hash Map & Frequency Sort)

---

## Problem Description
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

---

## Intuition & Approach
1. Count the frequency of each number using a hash map / dictionary.
2. Sort the unique elements by their frequencies in descending order.
3. Return the first `k` elements from the sorted list.

*(Note: Optimal bucket sort can achieve $\mathcal{O}(n)$ time).*

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n + m \log m)$ — Where $n$ is the length of `nums` and $m$ is the number of unique elements ($m \le n$).
- **Space Complexity**: $\mathcal{O}(m)$ — Hash map and sorted list store the unique elements.

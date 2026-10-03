# 🧠 Data Structures & Algorithms — Big Tech Interview Prep

Personal repository for Data Structures & Algorithms (DSA), competitive programming, and technical interview preparation for Big Tech (FAANG / Tier-1 tech companies).

Solutions are curated manually with clean code, type hints, edge case analysis, and asymptotic complexity ($\mathcal{O}$ Time & Space).

---

## 📊 Progress Dashboard

| # | Topic / Pattern | Solved | Status |
|:---:|:---|:---:|:---:|
| 01 | **Arrays & Hashing** | 3 | 🟡 In Progress |
| 02 | **Two Pointers** | 1 | 🟡 In Progress |
| 03 | **Sliding Window** | 0 | ⚪ Backlog |
| 04 | **Stack** | 0 | ⚪ Backlog |
| 05 | **Binary Search** | 2 | 🟡 In Progress |
| 06 | **Linked List** | 3 | 🟡 In Progress |
| 07 | **Trees** | 0 | ⚪ Backlog |
| 08 | **Tries** | 0 | ⚪ Backlog |
| 09 | **Heap / Priority Queue** | 0 | ⚪ Backlog |
| 10 | **Backtracking** | 0 | ⚪ Backlog |
| 11 | **Graphs** | 0 | ⚪ Backlog |
| 12 | **Advanced Graphs** | 0 | ⚪ Backlog |
| 13 | **1-D Dynamic Programming** | 0 | ⚪ Backlog |
| 14 | **2-D Dynamic Programming** | 0 | ⚪ Backlog |
| 15 | **Greedy** | 0 | ⚪ Backlog |
| 16 | **Intervals** | 0 | ⚪ Backlog |
| 17 | **Math & Geometry** | 0 | ⚪ Backlog |
| 18 | **Bit Manipulation** | 0 | ⚪ Backlog |

---

## 📚 Solved Problems Index

| # | Problem | Topic / Pattern | Source | Difficulty | Solution | Time | Space |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | [Contains Duplicate](01-arrays-and-hashing/contains-duplicate/) | Arrays & Hashing | LeetCode 217 / NeetCode 150 | `Easy` | [solution.py](01-arrays-and-hashing/contains-duplicate/solution.py) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| 2 | [Valid Anagram](01-arrays-and-hashing/valid-anagram/) | Arrays & Hashing | LeetCode 242 / NeetCode 150 | `Easy` | [solution.py](01-arrays-and-hashing/valid-anagram/solution.py) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 3 | [Group Anagrams](01-arrays-and-hashing/group-anagrams/) | Arrays & Hashing | LeetCode 49 / NeetCode 150 | `Medium` | [solution.py](01-arrays-and-hashing/group-anagrams/solution.py) | $\mathcal{O}(n \cdot k \log k)$ | $\mathcal{O}(n \cdot k)$ |
| 4 | [Two Sum II - Input Array Is Sorted](02-two-pointers/two-sum-ii-input-array-is-sorted/) | Two Pointers | LeetCode 167 / NeetCode 150 | `Medium` | [solution.py](02-two-pointers/two-sum-ii-input-array-is-sorted/solution.py) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 5 | [Binary Search](05-binary-search/binary-search/) | Binary Search | LeetCode 704 / NeetCode 150 | `Easy` | [solution.py](05-binary-search/binary-search/solution.py) | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ |
| 6 | [Koko Eating Bananas](05-binary-search/koko-eating-bananas/) | Binary Search (Answer Space) | LeetCode 875 / NeetCode 150 | `Medium` | [solution.py](05-binary-search/koko-eating-bananas/solution.py) | $\mathcal{O}(n \log m)$ | $\mathcal{O}(1)$ |
| 7 | [Reverse Linked List](06-linked-list/reverse-linked-list/) | Linked List | LeetCode 206 / NeetCode 150 | `Easy` | [solution.py](06-linked-list/reverse-linked-list/solution.py) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 8 | [Merge Two Sorted Lists](06-linked-list/merge-two-sorted-lists/) | Linked List | LeetCode 21 / NeetCode 150 | `Easy` | [solution.py](06-linked-list/merge-two-sorted-lists/solution.py) | $\mathcal{O}(n + m)$ | $\mathcal{O}(1)$ |
| 9 | [Linked List Cycle](06-linked-list/linked-list-cycle/) | Linked List | LeetCode 141 / NeetCode 150 | `Easy` | [solution.py](06-linked-list/linked-list-cycle/solution.py) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |

---

## 📁 Repository Structure

The repository is organized by **algorithmic pattern / topic** rather than by platform. This makes it source-agnostic and ready for problems from **LeetCode**, **NeetCode**, **HackerRank**, **Codeforces**, or real interview questions:

```text
├── 01-arrays-and-hashing/
│   ├── contains-duplicate/
│   │   ├── README.md          # Intuition, approach, complexity, and edge cases
│   │   └── solution.py        # Clean solution with type hints and test assertions
│   └── ...
├── 02-two-pointers/
├── 03-sliding-window/
├── ...
├── templates/
│   └── PROBLEM_TEMPLATE.md    # Template for quickly adding new problems
├── .gitignore
└── README.md
```

---

## 🛠️ Adding a New Problem

1. Create a folder under the relevant pattern directory:  
   `XX-topic-name/problem-name/`
2. Copy [`templates/PROBLEM_TEMPLATE.md`](templates/PROBLEM_TEMPLATE.md) into the new directory as `README.md` and document the intuition and complexity.
3. Add `solution.py` with standard typing annotations and local test assertions under `if __name__ == "__main__":`.
4. Update the **Solved Problems Index** and the **Progress Dashboard** in this root `README.md`.

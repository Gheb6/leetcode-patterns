# Course Schedule

- **Source**: LeetCode 207 / NeetCode 150
- **Links**: [LeetCode #207](https://leetcode.com/problems/course-schedule/) | [NeetCode](https://neetcode.io/problems/course-schedule)
- **Difficulty**: Medium
- **Pattern**: Graphs (Topological Sort / Kahn's Algorithm / Cycle Detection)

---

## Problem Description
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course $b_i$ first if you want to take course $a_i$.

- For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Example 1
```text
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

### Example 2
```text
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

### Constraints
- $1 \le \text{numCourses} \le 2000$
- $0 \le \text{prerequisites.length} \le 5000$
- $\text{prerequisites}[i]\text{.length} == 2$
- $0 \le a_i, b_i < \text{numCourses}$
- All the pairs prerequisites[i] are **unique**.

---

## Intuition & Approach
The courses and their prerequisites form a **directed graph** where each directed edge $b \to a$ represents the prerequisite dependency "take course $b$ before course $a$". Completing all courses is possible if and only if the graph has **no directed cycles** (i.e. it is a Directed Acyclic Graph, or DAG).

### Kahn's Algorithm for Topological Sort (BFS):
1. **Graph & In-degree Construction**:
   - Construct an adjacency list `graph` where `graph[b]` holds all courses $a$ that depend on $b$.
   - Maintain an `in_degree` array where `in_degree[a]` counts how many prerequisite courses must be completed before taking course $a$.
2. **Queue Initialization**:
   - Find all courses with `in_degree == 0` (courses that have no prerequisites) and push them into `my_deque`.
3. **BFS Processing**:
   - Maintain a counter `completed = 0`.
   - While `my_deque` is not empty:
     - Pop `curr = my_deque.popleft()` and increment `completed += 1`.
     - For each course `neighbour` that depends on `curr`:
       - Decrement its in-degree: `in_degree[neighbour] -= 1`.
       - If `in_degree[neighbour] == 0`, all its prerequisites have now been met. Enqueue `neighbour`.
4. **Cycle Validation**:
   - If `completed == numCourses`, all courses can be successfully taken.
   - If `completed < numCourses`, any unvisited nodes belong to a cycle or depend on a cycle, making completion impossible.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(V + E)$ — Where $V = \text{numCourses}$ and $E = \text{len(prerequisites)}$. Building the graph takes $\mathcal{O}(E)$, initializing the queue takes $\mathcal{O}(V)$, and the BFS traversal processes each vertex and edge at most once.
- **Space Complexity**: $\mathcal{O}(V + E)$ — Storing the adjacency list takes $\mathcal{O}(V + E)$, and the `in_degree` array plus `my_deque` store up to $V$ elements.

---

## Edge Cases Considered
- **No prerequisites** (`prerequisites = []`): All courses start with `in_degree = 0`, queue processes all $V$ courses, returns `True`.
- **Self-cycle / Direct cycle** (`[[0, 1], [1, 0]]`): Neither node reaches `in_degree = 0`, returns `False`.
- **Disconnected components**: Disconnected DAGs process smoothly; cycles in any sub-component prevent `completed == numCourses`.
- **Single course** (`numCourses = 1`): Directly valid.

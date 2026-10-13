# Task Scheduler

- **Source**: LeetCode 621 / NeetCode 150
- **Links**: [LeetCode #621](https://leetcode.com/problems/task-scheduler/) | [NeetCode](https://neetcode.io/problems/task-scheduler)
- **Difficulty**: Medium
- **Pattern**: Heap / Priority Queue (Max-Heap + Queue)

---

## Problem Description
You are given an array of CPU `tasks` represented by uppercase English letters, and a cooling interval `n`. Each CPU cycle executes either one task or remains idle.

Identical tasks must have at least `n` units of cooling time between them.

Return the minimum number of CPU intervals required to complete all tasks.

---

## Strategy & Approach
To minimize idle slots, greedily execute the task with the highest remaining frequency:
1. **Frequencies & Max-Heap**: Count task occurrences and store negative frequencies in a max-heap (`max_heap`).
2. **Cooldown Queue**: Use a `deque` (`my_deque`) to store cooling tasks as `(remaining_count, unlock_time)`.
3. **Simulation**:
   - Increment `time` by 1.
   - Pop the most frequent available task from `max_heap`.
   - If the task still has executions left, enqueue it with `unlock = time + n`.
   - If the front task in `my_deque` is ready (`unlock == time`), push it back into `max_heap`.
4. Stop when both `max_heap` and `my_deque` are empty.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(m)$ — where $m$ is the total number of tasks. Since the heap contains at most 26 distinct tasks, heap operations take $\mathcal{O}(\log 26) = \mathcal{O}(1)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ — at most 26 unique character counts stored in the hash map, heap, and cooldown queue.

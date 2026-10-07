# Design Twitter

- **Source**: LeetCode 355 / NeetCode 150
- **Links**: [LeetCode #355](https://leetcode.com/problems/design-twitter/) | [NeetCode](https://neetcode.io/problems/design-twitter-feed)
- **Difficulty**: Medium
- **Pattern**: Heap / Priority Queue & Hash Table

---

## Problem Description
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and see the `10` most recent tweets in the user's news feed.

Implement the `Twitter` class:
- `postTweet(userId, tweetId)`: Composes a new tweet.
- `getNewsFeed(userId)`: Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themselves. Tweets must be ordered from most recent to least recent.
- `follow(followerId, followeeId)`: The user with ID `followerId` follows the user with ID `followeeId`.
- `unfollow(followerId, followeeId)`: The user with ID `followerId` unfollows the user with ID `followeeId`.

---

## Intuition & Approach
- Maintain a global counter acting as a monotonic timestamp for each tweet.
- Store tweets per user in a hash map `tweet[userId] = [[userId, tweetId, timestamp], ...]`.
- Store following relationships in a hash map of sets `followers_map[userId] = set(...)`.
- To generate the news feed:
  1. Ensure the user follows themselves.
  2. Iterate through all tweets from the user and their followees.
  3. Maintain a **Min-Heap** bounded to size 10 ordered by timestamp `[timestamp, tweetId]`. When the heap size exceeds 10, pop the oldest tweet (`heapq.heappop`).
  4. Extract all elements from the heap and reverse to produce most recent first.

---

## Complexity Analysis
- **Time Complexity**:
  - `postTweet`: $\mathcal{O}(1)$
  - `getNewsFeed`: $\mathcal{O}(T \log 10) = \mathcal{O}(T)$ where $T$ is the number of tweets from followees (heap is bounded to 10 elements).
  - `follow` / `unfollow`: $\mathcal{O}(1)$ average set operations.
- **Space Complexity**: $\mathcal{O}(U + T_{\text{all}} + R)$ where $U$ is total users, $T_{\text{all}}$ total tweets stored, and $R$ total follow relationships.

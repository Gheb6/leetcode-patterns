"""
Problem: Design Twitter
LeetCode: 355 (https://leetcode.com/problems/design-twitter/)
NeetCode 150: Design Twitter (https://neetcode.io/problems/design-twitter-feed)
Difficulty: Medium
Pattern: Heap / Priority Queue & Hash Table
"""

from typing import List, Set
import heapq
from collections import defaultdict


class Twitter:
    """
    Time Complexity:
      - postTweet: O(1)
      - getNewsFeed: O(T log 10) where T is total tweets among user and followees (bounded min-heap of size 10)
      - follow: O(1)
      - unfollow: O(1)
    Space Complexity: O(U + T_all + R) where U is users, T_all total tweets, and R follow relationships.
    """

    def __init__(self):
        # Global counter to track chronological order of tweets
        self.global_counter = 0
        # Map userId to a list of their tweets: [userId, tweetId, timestamp]
        self.tweet = defaultdict(list)
        # Map userId to a set of followee IDs
        self.followers_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Create a new tweet with the current global timestamp
        new_tweet = [userId, tweetId, self.global_counter]
        self.tweet[userId].append(new_tweet)
        self.global_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # A user always follows themselves
        self.followers_map[userId].add(userId)
        min_heap = []
        
        # Gather tweets from the user and everyone they follow
        for following in self.followers_map[userId]:
            for tweet in self.tweet[following]:
                # tweet -> [userId, tweetId, timestamp]
                # Use positive timestamp so the min-heap naturally drops the oldest (smallest) timestamps
                my_tweet = [tweet[2], tweet[1]]
                
                # Push into the min-heap
                heapq.heappush(min_heap, my_tweet)
                # Keep only the 10 most recent tweets by popping the smallest (oldest) timestamp
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
                    
        # Extract the tweet IDs from the heap
        res = []
        while min_heap:
            timestamp, tweetId = heapq.heappop(min_heap)
            res.append(tweetId)
            
        # Reverse to get the most recent tweets first
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers_map[followerId].discard(followeeId)

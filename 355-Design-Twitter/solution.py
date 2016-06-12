import heapq
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetIndx = 0
        self.tweets = {}
        self.followers = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.tweets:
            self.tweets[userId].append((self.tweetIndx, tweetId))
        else:
            self.tweets[userId] = [(self.tweetIndx, tweetId)]
        self.tweetIndx += 1
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        if userId in self.tweets:
            for i in self.tweets[userId]:
                heapq.heappush(heap, i)
                if len(heap) > 10:
                    heapq.heappop(heap)
        if userId in self.followers:
            for i in self.followers[userId]:
                for j in self.tweets[i]:
                    heapq.heappush(heap, j)
                    if len(heap) > 10:
                        heapq.heappop(heap)
        if not heap:
            return []
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            if followerId in self.followers:
                self.followers[followerId].add(followeeId)
            else:
                self.followers[followerId] = set([followeeId])
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
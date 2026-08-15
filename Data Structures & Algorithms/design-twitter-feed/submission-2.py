import heapq


class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)

        heap = [] 
        for followee in self.following[userId]:
            tweets = self.tweets[followee]
            if tweets:
                idx = len(tweets) - 1
                timestamp, tweetId = tweets[idx]
                heapq.heappush(heap, (timestamp, tweetId, followee, idx))
        
        res = []

        while heap and len(res) < 10:
            _, tweetId, followee, idx = heapq.heappop(heap)

            res.append(tweetId)

            if idx > 0:
                idx -= 1
                timestamp, tweetId = self.tweets[followee][idx]
                heapq.heappush(heap, (timestamp, tweetId, followee, idx))
            
        return res
           

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
        

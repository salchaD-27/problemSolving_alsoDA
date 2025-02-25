class Twitter {
    private tweets: { userId: number, tweetId: number, timestamp: number }[];
    private followers: Map<number, Set<number>>;
    private time: number;
    constructor() {
        this.tweets = [];
        this.followers = new Map();
        this.time = 0;
    }
    postTweet(userId: number, tweetId: number): void {this.tweets.push({ userId, tweetId, timestamp: this.time++ });}
    getNewsFeed(userId: number): number[] {
        const followees = this.followers.get(userId) || new Set();
        followees.add(userId);
        return this.tweets
            .filter(tweet => followees.has(tweet.userId))
            .sort((a, b) => b.timestamp - a.timestamp)
            .slice(0, 10)
            .map(tweet => tweet.tweetId);
    }
    follow(followerId: number, followeeId: number): void {
        if (!this.followers.has(followerId)) {this.followers.set(followerId, new Set());}
        this.followers.get(followerId)!.add(followeeId);
    }
    unfollow(followerId: number, followeeId: number): void {
        this.followers.get(followerId)?.delete(followeeId);
    }
}
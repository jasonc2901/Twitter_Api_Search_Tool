import tweepy
from datetime import datetime
import os

#sets up the API KEYS/ACCESS TOKENS
auth = tweepy.OAuthHandler(os.environ.get('TWITTER_API_KEY'), os.environ.get('TWITTER_API_KEY_SECRET'))
auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'), os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))

#main function
def get_tweets(username,date1,date2):
    api = tweepy.API(auth)
        
    #user = input("Please enter the username you are searching for: \n")
    user = username

    #start = input("Please enter the start date in format YYYY-MM-dd: \n")
    start = date1
    startDate = datetime.strptime(start,'%Y-%m-%d')
    #end = input("Please enter the end date in format YYYY-MM-dd: \n")
    end = date2
    endDate =   datetime.strptime(end,'%Y-%m-%d')

    tweets = []
    tmpTweets = api.user_timeline(user)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet.text)

    while (tmpTweets[-1].created_at > startDate):
        tmpTweets = api.user_timeline(user, max_id = tmpTweets[-1].id)
        for tweet in tmpTweets:
            if tweet.created_at < endDate and tweet.created_at > startDate:
                tweets.append(tweet.text)

    return tweets

#calls the main function
if __name__ == "__main__":
    main()
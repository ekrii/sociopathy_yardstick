import pandas as pd 
import matplotlib.pyplot as plt 
import snscrape
import snscrape.modules.twitter as sntwitter




# exmaple
# user = zhusu
# user2 = samczsun

def get_tweets(userx, lookback):
    user_tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{userx}').get_items()):
        if i > lookback:
            break
        user_tweets.append([tweet.content, tweet.date])
    tweets_df1 = pd.DataFrame(user_tweets, columns=['Tweets', 'Date Created'])
    
    return tweets_df1 

def parse(tweets):
    self_ref = []
    self_ref_words = ["we", "I'd", "me"]
    for i in range(len(tweets)):
        for j in self_ref_words:
            if j in tweets.loc[i]['Tweets'].split():
                self_ref.append(tuple(tweets.loc[i]))
    self_ref = pd.DataFrame(self_ref, columns=['Tweets', 'Date Created'])
    return self_ref

def visual(user1, user2):
    x1 = [len(user1), len(user2)]
    fig, ax = plt.subplots()
    ind = ['user1', 'user2']
    ax.bar(ind, x1, color='Pink', width=0.8)
    plt.xlabel('Self referential tweets')
    plt.show()

if __name__ == '__main__':
    u1 = input("Who is your first user?: ")
    u2 = input("Who is your second user?: ")
    lookbackx = 1000    # configure here
    user1 = get_tweets(u1, lookbackx)
    user2 = get_tweets(u2, lookbackx)
    k = parse(user1)
    j = parse(user2)
    print(len(k))
    print(len(j))

    x1 = [len(k), len(j)]
    fig, ax = plt.subplots()
    ind = [f'{u1}', f'{u2}']
    ax.bar(ind, x1, color='Pink', width=0.8)
    ax.set_ylabel('Count')
    ax.set_xlabel('Users')
    for i in range(len(x1)):
        ax.text(ind[i], x1[i], x1[i])
    plt.title(f'Self referential tweets out of the last {lookbackx} tweets')
    plt.show()





    

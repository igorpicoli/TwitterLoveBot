import tweepy
import time

auth = tweepy.OAuthHandler('','')
auth.set_access_token('', '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

#Quantos segundos o bot espera por curtida
esperar = 5

verificacao = input("quer curtir algo? [s/n]: ")
if verificacao == "s":
    search = input("Digite o termo a curtir: ")
    twittar = input("Tuitar sobre? [s/n]: ")
    nrTweets = 50
    if twittar == "s":
        api = tweepy.API(auth)
        api.update_status('Hoje eu amo: ' + search)

    for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
        try:
            print('Tweet Liked')
            tweet.favorite()
            time.sleep(esperar)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopInteration:
            break

# Seguir todos que estão seguindo a conta
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

nrTweets = 500

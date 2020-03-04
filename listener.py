import tweepy

consumer_key = ''
consumer_secret = ''
acess_token = ''
acess_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acess_token_secret)
api = tweepy.API(auth)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.

x = ['Ziguirr', 'Rixadi404', 'Endeermon', 'Wellton404', 'GobiAndre',
            'pioshr', 'FSilvani_']

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=x)

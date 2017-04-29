
import speedtest, tweepy, os, time, sys, random

CONSUMER_KEY = os.environ['COMCAST_PLZ_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['COMCAST_PLZ_CONSUMER_SECRET']
ACCESS_KEY = os.environ['COMCAST_PLZ_ACCESS_KEY']
ACCESS_SECRET = os.environ['COMCAST_PLZ_ACCESS_SECRET']

greetings = ['Howdy, @Comcast', 'Hey @Comcast', '. @Comcast, you trickster', 'G\'day @Comcast', '. @Comcast, you old so-and-so', 'Hiya @Comcast!']


def DoTest(servers=[]):
	s = speedtest.Speedtest()
	print('Testing...')
	s.get_servers(servers)
	s.get_best_server()
	s.download()
	s.upload()

	results_dict = s.results.dict()
	return results_dict


def Complain(speed_test_results):
	download_mbps = round(speed_test_results['download']/1000000, 1)
	upload_mbps = round(speed_test_results['upload']/1000000, 1)

	if download_mbps <= 10:
		tweet_text = '{0} - I\'m paying for 25mbps download speeds and only getting {1}mbps. Sad! #Comcast #sad #speedtest'.format(random.choice(greetings), download_mbps)
		return tweet_text
	else:
		return None


def TweetAThing(text):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status(text)
	print(text)


def ComcastPlz():
	test = DoTest()
	c = Complain(test)
	if c:
		TweetAThing(c)


if __name__ == '__main__':
	while True:
		ComcastPlz()
		time.sleep(60*60)







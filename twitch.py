import requests


def channel_info(channel_name):
	return requests.get("https://api.twitch.tv/kraken/channels/{0}".format(channel_name)).json()


def followed_channels(user):
	return requests.get("https://api.twitch.tv/kraken/users/{0}/follows/channels".format(user), params = { "limit": 2147483647 }).json()["follows"]


def check_live(channel_names):
	if type(channel_names) == type(""):
		channel_names = [channel_names]
	live_channels = [stream["channel"]["name"] for stream in requests.get("https://api.twitch.tv/kraken/streams?channel={0}".format(",".join(channel_names))).json()["streams"]]
	return {channel_name: (channel_name in live_channels) for channel_name in channel_names}


if __name__ == "__main__":
	from pprint import pprint
	import sys
	channel = sys.argv[1] if len(sys.argv) > 1 else "jragon713"
	pprint(channel_info(channel))
	pprint(check_live([c["channel"]["name"] for c in followed_channels(channel)]))

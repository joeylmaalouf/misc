import praw
import time


r = praw.Reddit(user_agent="Subreddit Link Fixer by /u/Jragon713")
r.login("subreddit-link-fixer", "fixer-bot")
already_done = []
# i = 0

while True:
	# i += 1
	# print("Sweep #{0}".format(i))
	all_comments = r.get_comments("all")
	for comment in all_comments:
		if comment.id not in already_done:
			words = str(comment).split()
			for word in words:
				if word[:2].lower() == "r/":
					comment.reply("/"+word+"\n\n____\n\n^^Questions? ^^Contact ^^/u/Jragon713")
					print("Fixed \"{0}\"->\"/{0}\" by user {1}'s comment {2} on post {3} in /r/{4}".format(word, comment.author, comment.id, comment.submission.id, comment.subreddit))
					already_done.append(comment.id)
	time.sleep(2)

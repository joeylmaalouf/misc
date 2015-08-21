from collections import Counter
import praw
import sys


if __name__ == "__main__":
	r = praw.Reddit(user_agent = sys.argv[2] if len(sys.argv) > 2 else "flair_checker_user_agent")
	sr = r.get_subreddit(subreddit_name = sys.argv[1] if len(sys.argv) > 1 else "ssbpm")
	print("Parsing subreddit /r/{0}...".format(sr.display_name))
	old_id = ""
	posts = {}
	while True:
		for post in sr.get_new(limit = 25, params = {"after":old_id}):
			posts[post.fullname] = post
			# print("Post {0} - {1} points [{2}]: {3}".format(post.fullname, post.score, post.link_flair_text, post.title.encode("utf-8")))
		if old_id == post.fullname: # same id as last batch, so we found no new posts
			break
		old_id = post.fullname
	print("Parsed {0} most recent submissions.".format(len(posts)))
	print("Post Flairs:")
	flair_dict = Counter([post.link_flair_text for post in posts.values()])
	for flair, num in flair_dict.most_common():
		print("  {n} - {f}").format(n = num, f = flair)

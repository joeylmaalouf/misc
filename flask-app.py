from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
	return "Index Page"


@app.route("/hello/")
def hello():
	return "Hello World"


@app.route("/user/<username>/")
def show_user_profile(username):
	return "User {0}".format(username)


@app.route("/post/<int:post_id>/")
def show_post(post_id):
	if post_id in posts:
		return posts[post_id]
	else:
		return "Error: could not find post #{0}.".format(post_id)


if __name__ == "__main__":
	posts = {0: "hello", 1: "world", 2: ":D", 3: ":|"}
	app.run(host = "0.0.0.0", debug = True)
	# http://flask.pocoo.org/docs/0.10/quickstart/

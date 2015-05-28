from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
	return "This is the index page. <a href=\"post/0/\">Hello!</a>"


@app.route("/post/<int:post_id>/")
def show_post(post_id):
	post_str = posts[post_id] if post_id in posts else "Error: could not find post #{0}.".format(post_id)
	return post_str+"<br><a href=\"../"+str(max(0, post_id-1))+"\"><</a> <a href=\"../"+str(post_id+1)+"\">></a>"


if __name__ == "__main__":
	posts = {0: "hello", 1: "world", 2: ":D", 3: ":|"}
	app.run(host = "0.0.0.0", debug = True)
	# http://flask.pocoo.org/docs/0.10/quickstart/

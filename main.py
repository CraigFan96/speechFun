from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/profile/<name>')
def profile(name):
	return render_template("profile.html", name=name)


@app.route('/')
def index():
	return "Method used: %s" % request.method


"""
@app.route('/')
def index():
	return "Method used: %s" % request.method

@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
	if request.method == "POST":
		return "You are using POST"
	else:
		return 'You are probably using GET'


#Think of it as connecting an html link to the return response
@app.route('/tuna')
def tuna():
	return '<h2>Tuna is good</h2>'

@app.route('/profile/<username>')
def profile(username):
	return "<h2>Hey there</h2> %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "<h2>Post ID is %s</h2>" % post_id
"""


if __name__ == "__main__":
	app.run()
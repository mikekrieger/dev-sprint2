import flask, flask.views
import os
import functools

app = flask.Flask(__name__)

app.secret_key = "apple"

users = {'mike': 'apple'}

class Main (flask.views.MethodView):
	def get (self):
		return flask.render_template('index.html')

	def post (self):
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for ('index'))
		required = ['username', 'passwd']
		for r in required:
				if r not in flask.request.form:
					flask.flash("error: Invalid login information. (0) is required.".format(r))
					return flask.redirect(flask.url_for('index.html'))
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username] == passwd:
			flask.session['username'] = username
		else:
			flask.flash("Invalid login credentials")
		return flask.redirect(flask.url_for('index'))

def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("You must login to this system!")
			return flask.redirect(flask.url_for('index'))
	return wrapper


class Remote(flask.views.MethodView):
	def get(self):
		return flask.render_template('remote.html')

	@login_required
	def post(self):
		result = eval (flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))
		

app.add_url_rule('/',
	view_func=Main.as_view('index'),
	methods=["GET", "POST"])
app.add_url_rule('/remote/',
	view_func=Remote.as_view('remote'),
	methods=['GET', 'POST'])

app.debug = True
app.run()


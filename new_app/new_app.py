import flask, flask.views
import os

app = flask.Flask(__name__)

app.secret_key = "bacon"

class Main (flask.views.MethodView):
	def get (self):
		return flask.render_template('index.html')

	def post (self):
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			retrun flask.redirect(flask.url_for ('index'))
		required = ['username', 'passwd']
		for r in required:
				if r not in flask.request.form:
					flask.flash("error: Invalid login information. (0) is required.".format(r))
					return flask.redirect(flask.url_for('index'))
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username] == passwd:
			flask.session['username'] = username
		else:
			flask.flash("Invalid login credentials")
		return flask.redirect(flask.url_for('index'))


class View(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		result = eval (flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))
		

app.add_url_rule('/', 
				view_func=View.as_view('main'), 
				methods=['GET', 'POST'])

app.debug = True
app.run()

<link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen"><style.css>
<script type="text/javascript" src="/static/jquery-1.7.1.min.js"></script>
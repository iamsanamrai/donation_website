import os.path
from flask import Flask, jsonify, request, redirect, url_for, render_template 

app = Flask(__name__, static_url_path='/static')

# Main page Route link
@app.route('/')
def index():
	return render_template('index.html', title='20 by 20 fundtion')

@app.route('/home')
def home():
	return render_template('index.html', title='20 by 20 fundtion')

@app.route('/ideas')
def ideas():
	return render_template('ideas.html', title="20 by 20 funding ideas")

@app.route('/join-us')
def join_js():
	return render_template('join-us.html',  title="20 by 20 join-us mass funding")

@app.route('/login')
def login():
	return render_template('login.html',  title="20 by 20 login")

@app.route('/how-to-work')
def how_to_work():
	return render_template('how-to-work.html', title="20 by 20 mass funding how to work")

# After Login Inside page Routes link
@app.route('/login/insides')
def login_insides():
	user_name = "admin@gmail.com"
	userpwd = "password"
	return render_template('/insides/insides.html', username=user_name ,title="20 by 20 Mass funding inside")

@app.route('/logout')
def logout():
	return render_template('index.html', title="20 by 20  logout")


# Footer link Routes
@app.route('/privacy')
def privacy():
	return render_template('how-to-work.html', title="20 by 20 mass funding how to work")

@app.route('/terms')
def terms():
	return render_template('how-to-work.html', title="20 by 20 mass funding how to work")

@app.route('/guarantee-policy')
def guarentee_policy():
	return render_template('guarantee-policy.html', title="20 by 20 Mass Funding Guarantee policy")

@app.route('/desclaimer')
def desclaimer():
	return render_template('disclaimer.html',  title="20 by 20 Mass funding Desclaimer")

@app.route('/common-question')
def common_question():
	return render_template('common-question.html',  title="20 by 20 Mass fundtion common Questions")

# Application Run Section
app.run(port=5000)

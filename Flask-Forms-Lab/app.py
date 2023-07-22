from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Siraj"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/', methods = ['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		usr1 = request.form['username']
		psw1 = request.form['password']
		if usr1 == username and psw1 == password :
			return redirect(url_for('home'))
		else:
			return(render_template('login.html'))
  

@app.route('/home')
def home():
	return render_template('home.html', friends = facebook_friends)
  
@app.route('/friends_exist/<string:name>')
def friends_exist(name):	
	if name in facebook_friends:
		return render_template('friend_exists.html', value = True)
	else:
		return render_template('friend_exists.html', value = False)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)

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
	if methods == 'GET':
		return render_template('login.html')
	else:
		usr1 = request.form(username)
		psw1 = request.form(password)
		if usr1 == username and psw1 == password :
			return redirect(url_for(home.html))
  

@app.route('/home')
def home():
	return render_template('home.html', friends = facebook_friends)
  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)

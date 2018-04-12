from mitm import app
from flask import jsonify, request, render_template, flash

from utilities import Network_Utils, Utils
from forms import SplashForm

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
	if request.method == 'POST':
		if form.validate():
			params = Network_Utils.get_request_details(request)
			params["name"] = request.form['name']
			params["email"] = request.form['email']
			Utils.unblock_user(params)
			flash('Thanks for registration ' + name)
		else:
			flash('Error: All the form fields are required. ')

	return render_template("form.html", form=form)

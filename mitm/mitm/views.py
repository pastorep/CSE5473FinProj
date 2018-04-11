from mitm import app
from flask import jsonify, request

from utilities import Network_Utils

@app.route("/test")
def test():
	return jsonify(
		message="Test API working"
	)

@app.route("/")
def home():
	print(Network_Utils.get_request_details(request))
	return jsonify(
		message="Home page"
	)

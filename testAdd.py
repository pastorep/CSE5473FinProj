import mitmproxy
from mitmproxy.models import HTTPResponse
from netlib.http import Headers
import random
import re

def request(flow):
	print('FLAG')
	print(flow.request.pretty_host)
	addr = str(flow.client_conn.address)
	test = addr.find(':')
	addr = addr[:test]
	print(addr)

	# if flow.request.pretty_host == "mitm.it":
	# 	print('OK')

	params = {"ip": addr}

	# if flow.request.pretty_host is not '' and flow.request.pretty_host != "cache.marriott.com" and flow.request.pretty_host != "mitm.it" and flow.request.pretty_host != "localhost" and check_user_ip_exists(params):
	if flow.request.pretty_host is not '' and not check_user_ip_exists(params):
		flow.request.headers["org_ip"] = addr
		flow.request.host = "localhost"
		flow.request.port = 5000
		flow.request.scheme = 'http'
		print('MODIFIED')
		print(flow.request.host)

def response(flow):	
	if flow.response.headers.get("content-type", "").startswith("image"):
		namesArr = ["puppy.png","puppy1.jpg","pupp2.jpeg"]
		i = random.randint(0,len(namesArr) - 1)
		puppy_pic = open(namesArr[i], "rb").read()
		flow.response.content = puppy_pic
		#flow.response.headers["content-type"] = "image/png"

	if flow.response.headers.get("content-type", "").startswith("text/html"):
		tempText=flow.response.content
		print('RESPONSEtext')
		print(len(flow.response.content))
		print(flow.response.content)
		tempText = re.sub(r'\bThe\b','*woof*',tempText)
		tempText = re.sub(r'The\b','*woof*',tempText)
		flow.response.content = re.sub(r'\bthe\b','*woof*',tempText)		

def check_user_ip_exists(params):
    ip = params["ip"]
    with open("/var/lib/users", "r") as r:
        for line in r:
            line = line.strip()
            if line == ip:
                return True
	return False

#	print("CATCHINIT!")
#	print(flow.client_conn.address)
#	flow.request.host = "10.0.2.4"
#	flow.request.port = "5000"
#	flow.request.scheme = 'http'
#	flow.request.headers["Host"] = "10.0.2.4:5000"
#	flow.reply(HTTPResponse('HTTP/1.1', 302, 'Found', Headers(Location='http://#stackoverflow.com/',Content_Length='0'),b''))


	#method = flow.request.path.split('/')[3].split('?')[0]

	#if method == 'getjson':
       #flow.request.path=flow.request.path.replace(method,"getxml")

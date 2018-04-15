import mitmproxy
from mitmproxy.models import HTTPResponse
from netlib.http import Headers


def request(flow):
	print('FLAG')
	print(flow.request.pretty_host)
	print(flow.client_conn.address)
	addr = str(flow.client_conn.address)
	test = addr.find(':')
	addr = addr[:test]
	print(addr)

	if flow.request.pretty_host is not '':
		flow.request.host = "localhost"
		flow.request.port = 5000
		flow.request.scheme = 'http'
		print('MODIFIED')
		print(flow.request.host)

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
            



import mitmproxy
from mitmproxy.models import HTTPResponse
from netlib.http import Headers

def request(flow):
     print('FLAG')
     print(flow.request.pretty_host)
     if flow.request.pretty_host == "example.org":
         #flow.request.host = "10.0.2.4"
         flow.request.host = "google.com"
         #flow.request.port = "5000"


#    print("CATCHINIT!")
#    print(flow.client_conn.address)
#    flow.request.host = "10.0.2.4"
#    flow.request.port = "5000"
#    flow.request.scheme = 'http'    
#    flow.request.headers["Host"] = "10.0.2.4:5000"
#    flow.reply(HTTPResponse('HTTP/1.1', 302, 'Found', Headers(Location='http://#stackoverflow.com/',Content_Length='0'),b''))


    #method = flow.request.path.split('/')[3].split('?')[0]

    #if method == 'getjson':
       #flow.request.path=flow.request.path.replace(method,"getxml")
            



import mitmproxy
from mitmproxy.models import HTTPResponse
from netlib.http import Headers
def request(flow):
    print("CATCHINIT!")
    print(flow.client_conn.address)
    flow.request.host = "www.whipped.in"
    flow.request.scheme = 'http'    
    flow.request.headers["Host"] = "www.whipped.in"


    #method = flow.request.path.split('/')[3].split('?')[0]

    #if method == 'getjson':
       #flow.request.path=flow.request.path.replace(method,"getxml")
            



import mitmproxy
from mitmproxy.models import HTTPResponse
from netlib.http import Headers
def request(flow):

    if flow.request.pretty_host.endswith("mydomain.com"):
            mitmproxy.ctx.log( flow.request.path )
            method = flow.request.path.split('/')[3].split('?')[0]
            flow.request.host = "newsite.mydomain.com"
            flow.request.port = 8181
            flow.request.scheme = 'http'
            if method == 'getjson':
                flow.request.path=flow.request.path.replace(method,"getxml")
            flow.request.headers["Host"] = "newsite.mydomain.com"

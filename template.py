from mitmproxy import ctx
from mitmproxy import flow
import mitmproxy

def request(flow):
	addons.request(flow)
	
class Counter:
	def __init__(self):
		self.num = 0
		print("CONSTRUCTOR ")

	def request(self, flow):
		self.num = self.num + 1
		print("We've seen %d flows ", self.num)
		ctx.log.info("We've seen %d flows" % self.num)

	def response(self, flow):
		print("We've seen %d flows ", self.num)

	def http_connect(self, flow):
		print("HTTP CONNECT")


addons = Counter()


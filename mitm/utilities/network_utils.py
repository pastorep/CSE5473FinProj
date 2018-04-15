import subprocess
import shlex

import Constants

class Network_Utils:

    @staticmethod
    def get_request_details(request):
    	ip_address = request.remote_addr
    	return {
    		"ip": ip_address
    	}

    @staticmethod
    def extract_mac(stdout):
    	if stdout == None:
    		return None
    	if Constants.NO_ENTRY in stdout:
    		return None
    	lines = stdout.split("\n")
    	data = lines[1]
    	tokens = data.split()
    	return tokens[2]

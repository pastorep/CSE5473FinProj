import subprocess
import shlex

from .constants import Constants

class Network_Utils:

    @staticmethod
    def get_request_details(request):
    	ip_address = request.remote_addr
    	temp_ip_address = ip_address
    	popen = subprocess.Popen(shlex.split(Constants.ARP_LINUX_COMMAND + temp_ip_address), stdout=subprocess.PIPE)
    	stdout = popen.communicate()[0]
    	return {
    		"ip": ip_address,
    		"mac": Network_Utils.extract_mac(stdout)
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

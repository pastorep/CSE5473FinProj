import subprocess
import shlex
import time

from datetime import datetime

from .constants import Constants

class Utils:

    @staticmethod
    def run_rmtrack(ip_address):
    	subprocess.call(shlex.split(Constants.RMTRACK_LINUX_COMMAND + ip_address))

    @staticmethod
    def update_ip_table(mac_address):
        subprocess.call(shlex.split(Constants.UPDATE_IP_TABLE_LINUX_COMMAND_PART_1 + mac_address + Constants.UPDATE_IP_TABLE_LINUX_COMMAND_PART_2))

    @staticmethod
    def store_user_ip(params):
        data = params["ip"]
        with open(Constants.USER_STORE_FILE, "a+") as w:
            w.write(data)
            w.write("\n")

    @staticmethod
    def check_user_ip_exists(params):
        ip = params["ip"]
        with open(Constants.USER_STORE_FILE, "r") as r:
            for line in r:
                line = line.strip()
                if line == ip:
                    return True
        return False

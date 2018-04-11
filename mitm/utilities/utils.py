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
    def store_user(params):
        data = params["name"]
        data = data + "\t" + params["email"]
        data = data + "\t" + params["mac"]
        data = data + "\t" + params["ip"]
        data = data + "\t" + get_date()
        with open(Constants.USER_STORE_FILE, "a+") as w:
            w.write(data)
            w.write("\n")

    @staticmethod
    def unblock_user(params):
        store_user(params)
        update_ip_table(params["mac"])
        run_rmtrack(params["ip"])

    @staticmethod
    def get_date():
        time_tuple = datetime.now()
        string = time_tuple.strftime("YYYY-MM-DD")
        return string

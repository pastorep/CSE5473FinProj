class Constants:

    NO_ENTRY = "no entry"

    ARP_LINUX_COMMAND = "arp -n "
    RMTRACK_LINUX_COMMAND = "rmtrack "
    UPDATE_IP_TABLE_LINUX_COMMAND_PART_1 = "sudo iptables -I internet 1 -t mangle -m mac --mac-source "
    UPDATE_IP_TABLE_LINUX_COMMAND_PART_2 = " -j RETURN"

    USER_STORE_FILE = "/var/lib/users"

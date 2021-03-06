#Code taken from AndyBev.com
#Code modified by Patrick Pastore

IPTABLES=/sbin/iptables

# Create internet chain
# This is used to authenticate users who have already signed up
$IPTABLES -N internet -t mangle

# First send all traffic via newly created internet chain
# At the prerouting NAT stage this will DNAT them to the local
# webserver for them to signup if they aren't authorised
# Packets for unauthorised users are marked for dropping later
$IPTABLES -t mangle -A PREROUTING -j internet

###### INTERNET CHAIN ##########
# Allow authorised clients in, redirect all others to login webserver
# Add known users to the NAT table to stop their dest being rewritten
# Ignore MAC address with a * - these users are blocked
# This awk script goes through the /var/lib/users flat file line by line
#awk 'BEGIN { FS="\t"; } { system("$IPTABLES -t mangle -A internet -m mac --mac-source "$4" -j RETURN"); }' /var/lib/users

$IPTABLES -t mangle -A internet -m mac --mac-source 08:00:27:18:7e:52 -j RETURN
$IPTABLES -t mangle -A internet -s 10.0.2.200 -j RETURN
$IPTABLES -t mangle -A internet -s 127.0.0.1 -j RETURN
$IPTABLES -t mangle -A internet --destination 10.0.2.200 -j RETURN
$IPTABLES -t mangle -A internet --destination 127.0.0.1 -j RETURN

# MAC address not found. Mark the packet 99
$IPTABLES -t mangle -A internet -j MARK --set-mark 99
################################

# Redirects web requests from Unauthorised users to logon Web Page
$IPTABLES -t nat -A PREROUTING -m mark --mark 99 -p tcp --dport 80 -j DNAT --to-destination 127.0.0.1:5000


# Now that we've got to the forward filter, drop all packets
# marked 99 - these are unknown users. We can't drop them earlier
# as there's no filter table
$IPTABLES -t filter -A FORWARD -m mark --mark 99 -j DROP

# Do the same for the INPUT chain to stop people accessing the web through Squid
$IPTABLES -t filter -A INPUT -p tcp --dport 80 -j ACCEPT
$IPTABLES -t filter -A INPUT -p tcp --dport 443 -j ACCEPT
$IPTABLES -t filter -A INPUT -p udp --dport 53 -j ACCEPT
$IPTABLES -t filter -A INPUT -m mark --mark 99 -j DROP

# Enable Internet connection sharing
echo "1" > /proc/sys/net/ipv4/ip_forward
#Disable ICMP resends
sysctl -w net.ipv4.conf.all.send_redirects=0
$IPTABLES -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
$IPTABLES -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 8080
$IPTABLES -A FORWARD -i ppp0 -o eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPTABLES -A FORWARD -i eth0 -o ppp0 -j ACCEPT
$IPTABLES -t nat -A POSTROUTING -o ppp0 -j MASQUERADE

#Begin mitmproxy
mitmproxy -T
#!/bin/bash
for i in $( iptables -t nat --line-numbers -L | grep ^[0-9] | awk '{ print $1 }' | tac ); do iptables -t nat -D PREROUTING $i; done

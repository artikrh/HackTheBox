#!/usr/bin/python3
# -*- coding: utf-8 -*-
from web3 import Web3
from sys import exit
import os, time, json
import getpass, hashlib

CPURP = '\033[95m'
CGREEN = '\033[92m'
CRED = '\033[91m'
CEND = '\033[0m'

def load_contract():
    while True:
        with open('build/contracts/ChainsawClub.json') as f:
            contractData = json.load(f)

        try:
            w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:63991'))
            w3.eth.defaultAccount = w3.eth.accounts[0]
        except:
            print("Failed to establish a connection with Ganache! Exiting...")
            exit()

        Url = w3.eth.contract(abi=contractData['abi'],
                              bytecode=contractData['bytecode'])

        try:
            caddress = open("address.txt",'r').read()
            caddress = caddress.replace('\n', '')
        except:
            with open('address.txt', 'w') as f:
                tx_hash = \
                    Url.constructor().transact({'from': w3.eth.accounts[0]})
                tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
                caddress = tx_receipt.contractAddress
                f.write("{}\r\n".format(caddress))
                f.close()

        # Contract instance
        contractInstance = w3.eth.contract(address=caddress,
                                           abi=contractData['abi'])

        try:
            user = input("Username: ")
            pwd = getpass.getpass("Password: ")
        except KeyboardInterrupt:
            print("")
            exit()

        # Calling the function of contract
        username = contractInstance.functions.getUsername().call()
        password = contractInstance.functions.getPassword().call()

        if username.strip() or password.strip():
            p = hashlib.md5()
            p.update(pwd.encode('utf-8'))
            if username == user and password == p.hexdigest():
                approve = contractInstance.functions.getApprove().call()
                if approve == True:
                    balance = contractInstance.functions.getBalance().call()
                    if balance == 1000:
                        contractInstance.functions.reset().call()
                        inner_banner()
                        os.system("/bin/bash")
                    else:
                        print ("{}[*]{} Not enough funds!".format(CRED,CEND))
                else:
                    print ("{}[*]{} User is not approved!".format(CRED,CEND))
            else:
                print ("{}[*]{} Wrong credentials!".format(CRED,CEND))
        else:
            print ("{}[*]{} Blank credentials are not allowed!".format(CRED,CEND))

        try:
            time.sleep(5)
        except KeyboardInterrupt:
            print("")
            exit()

def outer_banner():
    msg = """{}
      _           _
     | |         (_)
  ___| |__   __ _ _ _ __  ___  __ ___      __
 / __| '_ \ / _` | | '_ \/ __|/ _` \ \ /\ / /
| (__| | | | (_| | | | | \__ \ (_| |\ V  V /
 \___|_| |_|\__,_|_|_| |_|___/\__,_| \_/\_/
                                            club
{}
- Total supply: 1000
- 1 CHC = 51.08 EUR
- Market cap: 51080 (€)

{}[*] Please sign up first and then log in!
[*] Entry based on merit.
""".format(CRED,CPURP,CEND)
    print(msg)

def inner_banner():
    msg = """
\t ************************
\t * {}Welcome to the club!{} *
\t ************************

{} Rule #1: Do not get excited too fast.{}
    """.format(CGREEN,CEND,CPURP,CEND)
    print(msg)

if __name__ == "__main__":
    outer_banner()
    load_contract()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
from web3 import Web3
import json, hashlib

def enter_club():
    # Store Ethereum contract address
    caddress = open("address.txt",'r').read()
    caddress = caddress.replace('\n', '')

    # Load Ethereum contract configuration
    with open('build/contracts/ChainsawClub.json') as f:
        contractData = json.load(f)

    # Establish a connection with the Ethereum RPC interface
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:63991'))
    w3.eth.defaultAccount = w3.eth.accounts[0]

    # Get Application Binary Interface (ABI) and Ethereum bytecode
    Url = w3.eth.contract(abi=contractData['abi'],
                          bytecode=contractData['bytecode'])
    contractInstance = w3.eth.contract(address=caddress,
                                       abi=contractData['abi'])

    # Phase I & II: Create a new account and confirm
    username = "artikrh"
    password = hashlib.md5()
    password.update("arti".encode('utf-8'))
    password = password.hexdigest()
    contractInstance.functions.setUsername(username).transact()
    contractInstance.functions.setPassword(password).transact()
    cusername = contractInstance.functions.getUsername().call()
    cpassword = contractInstance.functions.getPassword().call()
    print("[*] Added user: {}".format(cusername))
    print("[*] Password (MD5): {}".format(cpassword))

    # Phase III: Approve our user and confirm
    contractInstance.functions.setApprove(True).transact()
    approvalStatus = contractInstance.functions.getApprove().call()
    print("[*] Approval status: {}".format(approvalStatus))

    # Phase IV: Transfer needed funds of value 1000 and confirm
    contractInstance.functions.transfer(1000).transact()
    supply = contractInstance.functions.getSupply().call()
    balance = contractInstance.functions.getBalance().call()
    print("[*] Supply left: {}".format(supply))
    print("[*] Total balance: {}".format(balance))

if __name__ == "__main__":
    enter_club()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
from web3 import Web3
import os, subprocess, time, json
import runganache

def load_contract():
    oldDomain = "google.com"
    while True:
        # Load Ethereum contract configuration
        with open('/opt/WeaponizedPing/shared/WeaponizedPing.json') as f:
            contractData = json.load(f)

        # Establish Ethereum RPC interface
        w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:9810'))
        w3.eth.defaultAccount = w3.eth.accounts[0]

        # Get Application Binary Interface (ABI) and Ethereum bytecode
        Url = w3.eth.contract(abi=contractData['abi'],
                              bytecode=contractData['bytecode'])

        # Create new (or load current) smart contract address
        try:
            caddress = open("/opt/WeaponizedPing/shared/address.txt",'r').read()
            caddress = caddress.replace('\n', '')
        except:
            with open("/opt/WeaponizedPing/shared/address.txt", 'w') as f:
                tx_hash = \
                    Url.constructor().transact({'from': w3.eth.accounts[0]})
                tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
                caddress = tx_receipt.contractAddress
                f.write("{}\r\n".format(caddress))
                f.close()

        # Create contract instance
        contractInstance = w3.eth.contract(address=caddress,
                                           abi=contractData['abi'])

        # Calling the function of contract to ping the specified domain
        newDomain = contractInstance.functions.getDomain().call()
        if newDomain != oldDomain:
            subprocess.Popen(['ping -c 1 {}'.format(newDomain)], shell=True, stderr=subprocess.STDOUT)
        oldDomain = newDomain

        time.sleep(5)

def rmAddress():
    filename = 'shared/address.txt'
    if os.path.exists(filename):
        os.remove(filename)

if __name__ == "__main__":
    time.sleep(5) # Wait for ganache-cli to fully run
    rmAddress() # Remove previous smart contract address
    load_contract() # Deploy the ping service application

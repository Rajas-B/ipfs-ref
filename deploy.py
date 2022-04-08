from eth_typing import ContractName
from solcx import compile_standard, compile_files, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

install_solc('0.8.0')
with open("./SimpleStorage.sol", "r") as f:
    simple_storage_file = f.read()

# compiled_sol = compile_files(
#     ["./SimpleStorage.sol"],
#     output_values=["abi"],
#     solc_version="0.8.0"
#     )    
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version="0.8.0"
)
with open("compiled_code.json", "w") as f:
    json.dump(compiled_sol, f)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x20131cf62a1334E4cB66f61a5E27368De16C0f7e"
private_key = os.getenv("PRIVATE_KEY")

# Create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode = bytecode)

# Get latest transaction
nonce = w3.eth.getTransactionCount(my_address)

transaction = SimpleStorage.constructor().buildTransaction(
    {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
)

# sign transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

# Working with the contract, we need
# Contract address
# Contract ABI
simple_storage = w3.eth.contract(address=txn_receipt.contractAddress, abi=abi)

store_transaction = simple_storage.functions.addPerson("Rajas", ("Rajas", 256)).buildTransaction(
    {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce+1}
)

signed_store_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)

send_store_txn_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
send_store_txn_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn_hash)

print(simple_storage.functions.retrieveNumber("Rajas").call())
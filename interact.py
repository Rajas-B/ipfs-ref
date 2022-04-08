import json
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

# get simple storage contract
with open("compiled_code.json") as f:
    compiled_sol = json.load(f)


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x20131cf62a1334E4cB66f61a5E27368De16C0f7e"
private_key = os.getenv("PRIVATE_KEY")
nonce = w3.eth.getTransactionCount(my_address)

abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
contractAddress = "0xAcdfD03c33090690580d04Ea4785D4c2a47fEA81"

simple_storage = w3.eth.contract(address=contractAddress, abi=abi)

# store_transaction = simple_storage.functions.addPerson("Manas", ("Manas", 234)).buildTransaction(
#     {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
# )
# 
# signed_store_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
# 
# send_store_txn_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
# send_store_txn_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn_hash)

print(simple_storage.functions.retrieveNumber("Rajas").call())
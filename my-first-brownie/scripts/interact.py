from brownie import SimpleStorage, network, accounts, config

def get_account():
    if network.show_active() in ["development", "ganache-local"]:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def store_value():
    account = get_account()
    simple_storage = SimpleStorage[-1]
    transaction = simple_storage.addPerson("Rajas", ("Rajas", 256), {"from": account})
    transaction.wait(1)

def read_value():
    simple_storage = SimpleStorage[-1]
    number = simple_storage.retrieveNumber("Rajas")
    print(number)

def main():
    read_value()

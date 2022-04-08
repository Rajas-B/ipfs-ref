from brownie import accounts, config, SimpleStorage, network

def get_account():
    if network.show_active() in ["development", "ganache-local"]:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    transaction = simple_storage.addPerson("Rajas", ("Rajas", 256), {"from": account})
    transaction.wait(1)
    stored_value = simple_storage.retrievePerson("Rajas", {"from": account})
    print(stored_value)


def main():
    deploy_simple_storage()
from bip32utils import BIP32Key, BIP32_HARDEN
from mnemonic import Mnemonic
from tronapi import Tron


full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io'

tron = Tron(full_node=full_node,
        solidity_node=solidity_node,
        event_server=event_server)


TRON_PATH = 195
# test seed
default_seed = 'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about'
account = 0
change = 0
index = 0



def changeSeed(seed, account, change, address_index):
    m = BIP32Key.fromEntropy(Mnemonic.to_seed(seed))
    m = m.ChildKey(44 + BIP32_HARDEN)
    m = m.ChildKey(TRON_PATH + BIP32_HARDEN)
    m = m.ChildKey(account + BIP32_HARDEN)
    m = m.ChildKey(change)
    m = m.ChildKey(address_index)
    return m

HD = changeSeed(default_seed, account, change, index)

def setTronPK(pk):
    tron.private_key = pk
    tron.default_address = tron.address.from_private_key(pk).base58

setTronPK(HD.PrivateKey().hex())

while True:
    print ("""
    1. Show SEED/Account
    2. Change SEED
    3. Change Account
    4. Show Private Key
    5. Show Tron Address
    6. Get Balance
    7. Exit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        print("Account: {}\nSEED: {}\n".format(account, default_seed))
    elif ans=="2":
        default_seed = input("Type the new seed: ")
        HD = changeSeed(default_seed, account, change, index)
        setTronPK(HD.PrivateKey().hex())
    elif ans=="3":
        account = input("Type the new account index [0-10]: ")
        HD = changeSeed(default_seed, account, change, index)
        setTronPK(HD.PrivateKey().hex())
    elif ans=="4":
        print("Private key: {}".format(HD.PrivateKey().hex()))
    elif ans=="5":
        print("Tron Address: {}".format(tron.default_address.base58)) 
    elif ans=="6":
        print("Account Info: {}".format(tron.trx.get_account())) 
    elif ans=="7":
        print("_CryptoChain_ Tron SR")
        break 
    elif ans !="":
        print("\n Not Valid Choice Try again") 

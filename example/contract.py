class MyContract:
    def __init__(self, testnet, creator_addr, my_addr, amount):
        self._testnet = testnet

    def ping(self, who, amount):
        self._testnet.pay(who, amount)

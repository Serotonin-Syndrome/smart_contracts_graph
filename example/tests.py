import os
from time import sleep


def run_tests(generators, TestNet, MyContract):
    use_delays = not bool(os.getenv('PleaseNoDelays'))

    creator_addr = generators.gen_addr()
    contract_addr = generators.gen_addr()
    users = [generators.gen_addr() for _ in range(7)]

    balances = {creator_addr: 2001}
    for user in users:
        balances[user] = 952

    testnet = TestNet(balances)
    testnet.deploy(MyContract, contract_addr=contract_addr, creator_addr=creator_addr, amount=10)
    if use_delays:
        print('Please switch to the browser and press ENTER when ready for the demo:')
        input()
        sleep(1)
    for user in users:
        if use_delays:
            sleep(2)
        for i in range(3):
            testnet.call_method('ping', user, i + 1, ())
